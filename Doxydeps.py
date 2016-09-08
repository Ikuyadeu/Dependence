import sys
from GetDeps import GetDependencies
from git import Repo
import time
import csv
import os

argv = sys.argv
argc = len(argv)

if argc == 3:
    repopass = (argv[1]) # ファイルパス
    csvpass = (argv[2])
else:
    print("Usage: %s repopass" % argv[0])
    sys.exit()

doxygen_command = "doxygen GetDeps/source/.config"
depwriter = csv.writer(open(csvpass, "w", encoding="utf-8"), lineterminator="\n")
os.system(doxygen_command)
gd = GetDependencies.GetDependencies(depwriter)

repo = Repo(repopass)
branch_name = 'master'

for commit_no, item in enumerate(repo.iter_commits(branch_name)):
    print(commit_no)
    repo.git.checkout(item)
    os.system(doxygen_command)

    d = time.gmtime(item.committed_date)
    date = ("%d-%d-%d" % (d.tm_year, d.tm_mon, d.tm_mday))

    author = str(item.author).replace(",", "")
    is_merge = (len(item.parents) > 1)

    gd.set_commitinfo(commit_no, date, author, is_merge)
    gd.get_file_location(item.stats.files.keys())
    gd.get_deps()

    #if commit_no > 2:
    #    break