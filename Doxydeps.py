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

repo = Repo(repopass)
for item in repo.iter_commits('master', max_count=10):
  print ('==================================')
  print ("author: %s" % item.author)
  for file in item.stats.files.keys():
    gd = GetDependencies.GetDependencies(file)
    if gd.infdp():
        print('--------')
        print("file: %s" % file)
        print()
        gd.getdeps()