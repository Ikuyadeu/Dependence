import sys
import time
import csv
import os
from git import Repo
from GetDeps.get_dependencies import GetDependencies

ARGV = sys.argv
ARGC = len(ARGV)

if ARGC == 4:
    REPOPASS = (ARGV[1]) # ファイルパス
    CSVPASS = (ARGV[2])
    BRANCH_NAME = (ARGV[3])
else:
    print("Usage: %s repopass csvpass master_branch_name" % ARGV[0])
    sys.exit()

DOXYGEN_COMMAND = "doxygen GetDeps/source/.config"

REPO = Repo(REPOPASS)
DEP_WRITER = csv.writer(open(CSVPASS, "w", encoding="utf-8"), lineterminator="\n")
GD = GetDependencies(DEP_WRITER)
DEP_WRITER.writerow(("commitNo", "file_location", "date", "author", "is_merge", "kind"))

for commit_no, item in enumerate(REPO.iter_commits(BRANCH_NAME)):
    file_list = [x for x in item.stats.files.keys() if os.path.splitext(x)[1] == ".java"]
    if len(file_list) == 0:
        continue
    
    print(commit_no)
    #print(file_list)

    os.system(DOXYGEN_COMMAND)
    REPO.git.checkout(item)

    d = time.gmtime(item.committed_date)
    date = ("%d-%d-%d" % (d.tm_year, d.tm_mon, d.tm_mday))

    author = str(item.author).replace(",", "")
    is_merge = (len(item.parents) > 1)

    GD.set_commitinfo(commit_no, date, author, is_merge)
    GD.get_file_location(file_list)
    GD.get_deps()
    break
