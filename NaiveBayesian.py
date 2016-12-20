import sys
import csv
import math
import re
from git import Repo
import treetaggerwrapper

ARGV = sys.argv
ARGC = len(ARGV)

if ARGC == 4:
    REPO_PASS =  (ARGV[2]) + (ARGV[1]) # ?t?@?C???p?X
    CSV_PASS = "DepsR\\" + (ARGV[1]) + "\\"
    BRANCH_NAME = (ARGV[3])
else:
    print("Usage: %s repopass csvpass master_branch_name" % ARGV[0])
    sys.exit()

KIND_NAMES = ["e", "ee", "er", "r", "rr", "re", "o"]

tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='C:\TreeTagger')

def getwords(doc):
    tags = treetaggerwrapper.make_tags(tagger.tag_text(doc), exclude_nottags=True)
    #return [x.lemma for x in tags if not re.search("[0-9a-f]{10,}|[^0-9A-Za-z]", x.lemma)]
    tags = [x.lemma for x in tags if not re.search("[0-9a-f]{10,}|[^0-9A-Za-z]", x.lemma)]
    return  [tags[0]] if len(tags) > 0 else list()
  
def wordcountup(doc, wordcount):
    counted = {}
    words = getwords(doc)
    for word in words:
        if word not in counted:
            wordcount[word] = wordcount[word] + 1 if word in wordcount else 1
            counted[word] = 1
    return wordcount

#def probscore(word, cat):
#    score = math.log(priorprob(cat))
#    for w in word:
#        score += math.log(wordprob(w, cat))
#    return score

word_count = {}
row_num = 0
csv_name = CSV_PASS + "message.csv"
with open(csv_name, encoding="utf-8") as csvfile:
    rows = 0
    reader = csv.DictReader(csvfile, lineterminator="\n", quoting=csv.QUOTE_ALL)
    for row in [x['message'] for x in reader]:
        word_count = wordcountup(row, word_count)
        rows += 1
    row_num = rows
    print(row_num)
print(len(word_count))

for kind in KIND_NAMES:
    word_kind_count = {}
    csvname = CSV_PASS + kind + "message.csv"
    csvname_w = CSV_PASS + kind + "messager.csv"
    with open(csvname, encoding="utf-8") as csvfile:
        dep_writer = csv.writer(open(csvname_w, "w", encoding="utf-8"), lineterminator="\n")
        kind_reader = csv.DictReader(csvfile)
        kind_message = [x['message'] for x in kind_reader if x['iskind'] == 'TRUE']
        kind_num = len(kind_message)
        p_kind = float(kind_num) / row_num
        print(p_kind)

        for row in kind_message:
            word_kind_count = wordcountup(row, word_kind_count)
            #dep_writer.writerow((row['commit_no'], row['iskind'], row['message'], probscore(self, row['message'])))

        for word, score in word_kind_count.items():
            word_kind_count[word] = float(score) / kind_num * p_kind / (float(word_count[word]) / row_num) 
        
        # 出力
        dep_writer.writerow(('word', 'score'))
        for word, score in sorted(word_kind_count.items(), key=lambda x:x[1], reverse=True):
            dep_writer.writerow((word, score))