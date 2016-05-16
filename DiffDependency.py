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
    if kindref == "compound":
        return "class"

    for member in indexroot.findall('./compound/member'):
        if member.get('refid') == refid:
            return member.get('kind')
    
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

dependency_array = {}

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
            kindref = ref.get('kindref')
            reftext = ref.text
            if refid not in dependency_array:
                dependency_array[refid] = Dp.Dependency(refid, kindref, lineno, reftext)
                kind = id_to_kind(refid ,dependency_array[refid].get_kindref(), indexroot)
                dependency_array[refid].set_kind(kind)
           
for id, dependency in dependency_array.items():
    print(dependency.get_lineno(), dependency, dependency.get_kind())