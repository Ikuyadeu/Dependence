import sys
import time
import csv
import os
from GetDeps import GetDependencies
from git import Repo

ARGV = sys.argv
ARGC = len(ARGV)

if ARGC == 4:
    REPOPASS = (ARGV[1]) # ファイルパス
    CSVPASS = (ARGV[2])
    BRANCH_NAME = (ARGV[3])
else:
    print("Usage: %s repopass" % ARGV[0])
    sys.exit()

DOXYGEN_COMMAND = "doxygen GetDeps/source/.config"

REPO = Repo(REPOPASS)
DEPWRITER = csv.writer(open(CSVPASS, "w", encoding="utf-8"), lineterminator="\n")
GD = GetDependencies.GetDependencies(DEPWRITER)

for commit_no, item in enumerate(REPO.iter_commits(BRANCH_NAME)):
    print(commit_no)
    os.system(DOXYGEN_COMMAND)
    REPO.git.checkout(item)

    d = time.gmtime(item.committed_date)
    date = ("%d-%d-%d" % (d.tm_year, d.tm_mon, d.tm_mday))

    author = str(item.author).replace(",", "")
    is_merge = (len(item.parents) > 1)

    GD.set_commitinfo(commit_no, date, author, is_merge)
    GD.get_file_location(item.stats.files.keys())
    GD.get_deps()
