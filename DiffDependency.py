import sys
import xml.etree.ElementTree as ET
from DependencyClass import Dependency as Dp
from DependencyClass import CompoundDependency as CDp
import DependencyIndex as DpI
 
def ref_to_XMLname(refid: str):
    """refidからXMLファイル名を生成
    Args:
        refid:refのid
    Returns:
        XMLのファイル名
    """
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

    
# git blameを利用してレビュアーを分析
def related_reviewer(linepass):
    pass
    
# 参加したレビュアーに対して要素ごとにカウントを付加
def count_reviewers_exp(reviewer, paraname):
    pass

argv = sys.argv
argc = len(argv)

if argc == 4:
    filename = (argv[1]) # ファイル名
    sline = int(argv[2]) # 変更開始行
    eline = int(argv[3]) # 変更終了行
else:
    print("Usage: %s filename startlineNomber endlineNumber" % argv[0])
    sys.exit()

dependency_dict = {} # すべての依存関係の辞書
call_dd = {}
called_dd = {}

# raw文字列(r)にしておくとエスケープが無効になる
doxygenfile = r'source\doxygen\xml\\'
indexfile = ref_to_XMLname('index')

index = DpI.DependencyIndex(indexfile) 

fileref = index.get_file_ref(filename)

if fileref is None:
    sys.exit()

filename = ref_to_XMLname(fileref)
root = ET.parse(filename).getroot()

# 値の設定
for compounddef in root.findall('./compounddef'):
    compoundname = compounddef.find('compoundname').text
    innerclass = compounddef.find('innerclass')
    innerclass_refid = innerclass.get('refid')
    print(compoundname, innerclass.text)
    
    # ファイルの場所を出力
    for location in compounddef.findall('./location'):
        file = location.get('file')
        print("file = %s" % file)

    # 依存関係を収集
    for line in compounddef.findall("./programlisting/codeline"):
        lineno = int(line.get("lineno"))
    
        if lineno < sline:
            continue
        elif lineno > eline:
            break
        
        for ref in line.findall('./highlight/ref'):
            refid = ref.get('refid')
            if refid in dependency_dict:
                continue
                
            kindref = ref.get('kindref')
            reftext = ref.text
            kind = index.id_to_kind(refid , kindref)
            compound = index.ref_to_compound(refid, kindref)
            dependency_dict[refid] = Dp.Dependency(refid, reftext, lineno, kind, compound)

output_dependency(filter_dict_kind(dependency_dict, "class"))
output_dependency(filter_dict_kind(dependency_dict, "function"))
output_dependency(filter_dict_kind(dependency_dict, "variable"))

#for called_compound in filter_dict_kind(dependency_dict, "class"):
for call_compound in index.get_root().findall('./compound'):
    filename = ref_to_XMLname(call_compound.get('refid'))
    compound = CDp.CompoundDependency(filename)
    compound.search_dependencylist()

    for cd in compound.get_dependency_list():
            print(cd)