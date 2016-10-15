import sys
import time
import csv
import os
import datetime
from git import Repo
from GetDeps.get_dependencies import GetDependencies

ARGV = sys.argv
ARGC = len(ARGV)

if ARGC == 4:
    REPO_PASS = (ARGV[1]) # ファイルパス
    CSV_PASS = (ARGV[2])
    BRANCH_NAME = (ARGV[3])
else:
    print("Usage: %s repopass csvpass master_branch_name" % ARGV[0])
    sys.exit()

DOXYGEN_COMMAND = "doxygen GetDeps/source/.config"

REPO = Repo(REPO_PASS)
DEP_WRITER = csv.writer(open(CSV_PASS, "w", encoding="utf-8"), lineterminator="\n")
DEP_WRITER.writerow(("commitNo", "file_location", "date", "author", "is_merge", "kind"))

KIND_NAME = ["root", "e", "ee", "er", "r", "rr", "re", "o"]
COMMITS_LEN = len(list(REPO.iter_commits(BRANCH_NAME)))

print("Start", datetime.datetime.today())

for commit_no, item in enumerate(REPO.iter_commits(BRANCH_NAME)):
    file_list = [x for x in item.stats.files.keys() if os.path.splitext(x)[1] == ".java"]
    flistlen = len(file_list)
    if flistlen == 0:
        continue

    REPO.git.checkout(item)

    sys.stdout.write("\r%d/%d commits %d files Running Doxygen..."
                     % (commit_no, COMMITS_LEN, flistlen))
    os.system(DOXYGEN_COMMAND)
    sys.stdout.write("\r%d/%d commits %d files Get Dependencies..."
                     % (commit_no, COMMITS_LEN, flistlen))

    d = time.gmtime(item.committed_date)
    date = ("%d-%d-%d" % (d.tm_year, d.tm_mon, d.tm_mday))

    author = str(item.author).replace(",", "")
    is_merge = (len(item.parents) > 1)
    get_dep = GetDependencies()
    get_dep.get_file_location(file_list)
    sys.stdout.write("\r%d/%d commits %d files Output Dependency..."
                     % (commit_no, COMMITS_LEN, flistlen))

    for (dep_files, kind) in zip(get_dep.get_deps(), KIND_NAME):
        for dep_file in dep_files:
            DEP_WRITER.writerow((commit_no, dep_file, date, author, is_merge, kind))
