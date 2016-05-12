import sys
import xml.etree.ElementTree as ET

# 変更されたファイルと行の定義
def diffFileLine(gitdata):
    pass
    
# ファイル・行から参照するxmlファイル名を生成
def makeXMLName(linepass):
    pass
    
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

if argc == 3:
    sline = int(argv[1])
    eline = int(argv[2])
else:
    print("Usage: %s startlineNomber endlineNomber" % argv[0])
    sys.exit()


# raw文字列(r)にしておくとエスケープが無効になる
filename = r'source\doxygen\xml\_calc_graduation_8java.xml'
tree = ET.parse(filename)
root = tree.getroot()

for location in root.iter('location'):
    file = location.get('file')
    print("file = %s" % file)

for line in root.iter('codeline'):
    lineno = int(line.get("lineno"))
    
    if lineno < sline:
        continue
    elif lineno > eline:
        break
        
    for ref in line.iter('ref'):
        refid = ref.get('refid')
        kindref = ref.get('kindref')
        print(lineno, refid, kindref)
