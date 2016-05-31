import sys
import xml.etree.ElementTree as ET
from DependencyClass import CompoundDependency as CDp
from DependencyClass import FileDependency as FDp
from DependencyClass import IndexDependency as IDp
 
argv = sys.argv
argc = len(argv)

if argc == 2:
    filepass = (argv[1]) # ファイルパス
else:
    print("Usage: %s filename" % argv[0])
    sys.exit()

# 依存関係のindexを生成
index = IDp.IndexDependency('index') 

# ファイルのrefを取得
fileref = index.get_file_ref(filepass)

if fileref is None:
    print("can't find %s" % repr(filepass))
    sys.exit()

fdp = FDp.FileDependency(fileref) # ファイルの依存
filedict = {} # 依存ファイルの辞書

print("依存しているファイル")
cy = {}
for id, dp in fdp.get_dependency().items():
    print(dp.get_location())
    if id not in filedict:
        filedict[id] = dp
        cy[id] = dp

print("\n依存されているファイル")
ed = {}
for id, dp in fdp.get_dependencied().items():
    print(dp.get_location())
    if id not in filedict:
        filedict[id] = dp
        ed[id] = dp

print("\n依存しているファイルに依存されているファイル")
cyed = {}

for __, dp in cy.items():
    ref2 = index.get_file_ref(dp.get_location())
    fdp2 = FDp.FileDependency(ref2)
    for id, dp2 in fdp2.get_dependencied().items():
        if id not in filedict and id not in cyed:
            cyed[id] = dp2
            filedict[id] = dp2

for __, dp in cyed.items():
    print(dp.get_location())

print("\n依存されているファイルに依存しているファイル")
edcy = {}

for __, dp in ed.items():
    ref2 = index.get_file_ref(dp.get_location())
    fdp2 = FDp.FileDependency(ref2)
    for id, dp2 in fdp2.get_dependency().items():
        if id not in filedict and id not in edcy:
            edcy[id] = dp2
            filedict[id] = dp

for __, dp in edcy.items():
    print(dp.get_location())