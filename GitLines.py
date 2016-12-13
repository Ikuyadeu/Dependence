import sys
import csv
import os
from git import Repo

ARGV = sys.argv
ARGC = len(ARGV)

if ARGC == 4:
    REPO_PASS =  (ARGV[2]) + (ARGV[1]) # �t�@�C���p�X
    CSV_PASS = "DepsR\\" + (ARGV[1]) + "\\lines.csv"
    BRANCH_NAME = (ARGV[3])
else:
    print("Usage: %s repopass csvpass master_branch_name" % ARGV[0])
    sys.exit()

REPO = Repo(REPO_PASS)

WRITER = csv.writer(open(CSV_PASS, "w", encoding="utf-8"), lineterminator="\n")
WRITER.writerow(("commit_no", "file_path", "deletions", "insertions", "lines"))

for commit_no, item in enumerate(REPO.iter_commits(BRANCH_NAME)):
    for file_path, lines in item.stats.files.items():
        if os.path.splitext(file_path)[1] == ".java":
            WRITER.writerow((commit_no, file_path, lines["deletions"], lines["insertions"], lines["lines"]))

