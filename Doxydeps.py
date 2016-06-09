import sys
from GetDeps import GetDeps

argv = sys.argv
argc = len(argv)

if argc == 3:
    filepass = (argv[1]) # ファイルパス
    authorname = (argv[2])
else:
    print("Usage: %s filename authorname" % argv[0])
    sys.exit()

gd = GetDeps.GetDeps(filepass)
gd.getdeps()