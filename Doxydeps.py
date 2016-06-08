import sys
import xml.etree.ElementTree as ET
from DependencyClass import CompoundDependency as CDp
from DependencyClass import FileDependency as FDp
from DependencyClass import IndexDependency as IDp
from Util import Util
 
argv = sys.argv
argc = len(argv)

if argc == 3:
    filepass = (argv[1]) # ファイルパス
    authorname = (argv[2])
else:
    print("Usage: %s filename authorname" % argv[0])
    sys.exit()

# 依存関係のindexを生成
index = IDp.IndexDependency('index') 

# ファイルのrefを取得
fileref = index.get_file_ref(filepass)

if fileref is None:
    print("can't find %s" % repr(filepass))
    sys.exit()


def file_to_depdict(root_dict:dict, is_to_dep:bool):
    dep_dict = {}
    for dep in root_dict.values():
        ref = index.get_file_ref(dep.get_location())
        fdp = FDp.FileDependency(ref)
        get_dep = fdp.get_dependency() if is_to_dep else fdp.get_dependencied()

        for id, dp2 in get_dep.items():
            if not (id in root_dict or id in dep_dict):
                dep_dict[id] = dp2


    return dep_dict

def output_dep(file_dict:dict, state):
    for no, dp in enumerate(file_dict.values()):
        print("%s, %s" % (dp.get_location(), state))


fdp = FDp.FileDependency(fileref) # ファイルの依存

# from(依存されている)ファイルの辞書
ed = file_to_depdict({fileref:fdp}, False)
output_dep(ed, "from")

# to(依存している)
cy = file_to_depdict({fileref:fdp}, True)
output_dep(cy, "to")

# from(依存されているものに)_from(依存されている)
ed2 = file_to_depdict(ed, False)
output_dep(ed2, "from_from")

# from(依存されているものに)_to(依存している)
ed2 = file_to_depdict(ed, True)
output_dep(ed2, "from_to")

cy2 = file_to_depdict(cy, False)
output_dep(cy2, "to_from")

cy2 = file_to_depdict(cy, True)
output_dep(cy2, "to_to")
