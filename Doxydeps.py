import sys
from GetDeps import GetDependencies
from git import *
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
    open
writer = csv.writer(open(csvpass, "w", encoding="utf-8"), lineterminator="\n")
depwriter = csv.writer(open("dep.csv", "w", encoding="utf-8"), lineterminator="\n")
gd = GetDependencies.GetDependencies(depwriter)

repo = Repo(repopass)

for commit_no, item in enumerate(repo.iter_commits('master')):
    repo.git.checkout(item)
    os.system("doxygen GetDeps/source/.config")
    d = time.gmtime(item.committed_date)
    date = ("%d-%d-%d" % (d.tm_year, d.tm_mon, d.tm_mday))

    for file in item.stats.files.keys():
        file_loc = gd.get_file_location(file)
        if file_loc != None:
            writer.writerow((commit_no, file_loc, date, "root"))
            if len(item.parents) > 1:
                gd.get_deps(file, commit_no, date)