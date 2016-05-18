import sys
import xml.etree.ElementTree as ET
import Dependency as Dp
 
def ref_to_XMLname(refid):
    """refidからXMLファイル名を生成
    Args:
        refid:refのid
    Returns:
        XMLのファイル名
    """
    return doxygenfile + refid + r".xml"


def get_file_ref(filename, indexroot):
    """ファイル名からファイルのrefidを探す
    Args:
        filename:検索するファイル名
        indexroot:検索するindexのroot
    Return:
        ファイルのrefid
    """
    for compound in indexroot.findall('./compound'):
        if compound.get('kind') == "file" and filename == compound.find('name').text:
            return compound.get('refid')

    return None

def id_to_kind(refid, kindref,indexroot):
    """refidからrefの種類(class, function, variable)を取得する
    Args:
        refid:検索するid
        kindref:memberかcompoundかの種類
        indexroot:検索するindexのroot
    Return:
        refの種類(class, function, variable)
    """
    
    findtag = './compound'
    if kindref == "member":
        findtag += '/member'

    for member in indexroot.findall(findtag):
        if member.get('refid') == refid:
            return member.get('kind')

def output_by_kind(dd, kind):
    print(kind)
    kind_dependency = dict(((id, dd[id]) for id in dd if dd[id].get_kind() == kind))
    
    if len(kind_dependency) == 0:
        print(None)
        return

    print("lineno, text")
    for id, dependency in kind_dependency.items():
        print(dependency.get_lineno(), dependency)
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

dependency_dict = {}

# raw文字列(r)にしておくとエスケープが無効になる
doxygenfile = r'source\doxygen\xml\\'
indexfile = ref_to_XMLname('index')
indexroot = ET.parse(indexfile).getroot()
fileref = get_file_ref(filename, indexroot)

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
    

    for location in compounddef.findall('./location'):
        file = location.get('file')
        print("file = %s" % file)

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
            kind = id_to_kind(refid , kindref, indexroot)
            dependency_dict[refid] = Dp.Dependency(refid, reftext, lineno, kind)

output_by_kind(dependency_dict, "class")
output_by_kind(dependency_dict, "function")
output_by_kind(dependency_dict, "variable")