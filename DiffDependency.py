import sys
import xml.etree.ElementTree as ET
from _collections import defaultdict
import Dependency as Dp

# 変更されたファイルと行の定義
def diffFileLine(gitdata):
    pass
    
# ファイル・行から参照するxmlファイル名を生成
def makeXMLName(filename):
    return filename
    
# 解析するxmlファイルを開く
def openXML(filename):
    pass
    
# 関係のあるcodeline=xのxを利用して見つける
def parseXML(file):
    pass
    
#  要素のオブジェクトを生成
def makeParamaterObject(paraname):
    pass
    
# git blameを利用してレビュアーを分析
def relatedReviewer(linepass):
    pass
    
# 参加したレビュアーに対して要素ごとにカウントを付加
def countReviewersExp(reviewer, paraname):
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

dependency_array = defaultdict(Dp.Dependency)

# raw文字列(r)にしておくとエスケープが無効になる
filename = makeXMLName(filename)
filename = r'source\doxygen\xml\_calc_graduation_8java.xml'
tree = ET.parse(filename)
root = tree.getroot()

# 値の設定
for compounddef in root.findall('./compounddef'):
    compoundname = compounddef.find('compoundname').text
    innerclass = compounddef.find('innerclass')
    innerclassid = innerclass.get('refid')
    innnerclass_prot = innerclass.get('prot')
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
            dependency_array[refid] = Dp.Dependency(refid, kindref, lineno, reftext)
            #print(dependency_array[refid].get_lineno(), dependency_array[refid], dependency_array[refid].get_kindref())

for id, dependency in dependency_array.items():
    print(dependency.get_lineno(), dependency._text, id, dependency.get_kindref())