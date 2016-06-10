import sys
from GetDeps import GetDependencies
from git import *
import time

argv = sys.argv
argc = len(argv)

if argc == 2:
    repopass = (argv[1]) # ファイルパス
else:
    print("Usage: %s repopass" % argv[0])
    sys.exit()


gd = GetDependencies.GetDependencies()

repo = Repo(repopass)

for commit_no, item in enumerate(repo.iter_commits('master', max_count=10)):
    d = time.gmtime(item.committed_date)
    date = ("%d-%d-%d" % (d.tm_year, d.tm_mon, d.tm_mday))

    for file in item.stats.files.keys():
        file_loc = gd.get_file_location(file)
        if file_loc != None:
            print("%d, %s, %s, root" % (commit_no, file_loc, date))

            if len(item.parents) > 1:
                gd.get_deps(file, commit_no, date)