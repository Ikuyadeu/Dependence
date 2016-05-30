import sys
import xml.etree.ElementTree as ET
from DependencyClass import Dependency as Dp
from DependencyClass import CompoundDependency as CDp
from DependencyClass import FileDependency as FDp
from DependencyClass import IndexDependency as IDp
 
def ref_to_XMLname(refid: str):
    """refidからXMLファイル名を生成
    Args:
        refid:refのid
    Returns:
        XMLのファイル名
    """
    doxygenfile = r'source\doxygen\xml\\'
    return doxygenfile + refid + r".xml"

def filter_dict_kind(dd, kind):
    return dict(((id, dd[id]) for id in dd if dd[id].get_kind() == kind))

def output_dependency(dependency_dict: dict):
    """ 依存関係を出力
    
    """
    if len(dependency_dict) == 0:
        print(None)
        return

    print("lineno, text")
    for __, dependency in dependency_dict.items():
        print(dependency.get_lineno(), dependency, dependency.get_compound())
    print()


argv = sys.argv
argc = len(argv)

if argc == 2:
    filename = (argv[1]) # ファイル名
else:
    print("Usage: %s filename" % argv[0])
    sys.exit()

# indexを生成
index = IDp.IndexDependency('index') 

# ファイルのrefを取得
fileref = index.get_file_ref(filename)

if fileref is None:
    sys.exit()

fdp = FDp.FileDependency(fileref)
fdp.get_dependency()
fdp.output_dependency_dict()