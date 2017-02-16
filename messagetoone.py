import sys
import csv
import re
from collections import Counter
import treetaggerwrapper

ARGV = sys.argv
ARGC = len(ARGV)

if ARGC == 4:
    CSV_PASS = "DepsR\\" + (ARGV[1]) + "\\"
else:
    print("Usage: %s repopass csvpass master_branch_name" % ARGV[0])
    sys.exit()

    
project_name = ["vert.x","egit","egit-github"]

tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='C:\TreeTagger')
def getwords(doc):
    tags = [x.lemma for x in treetaggerwrapper.make_tags(tagger.tag_text(doc), exclude_nottags=True) if not re.search("[0-9a-f]{10,}|[^0-9A-Za-z]", x.lemma)]
    return  tags[0] if len(tags) > 0 else None

for project in project_name:
    print(project)
    csvpass = "DepsR\\" + project + "\\"
    csvname = csvpass + "message.csv"
    with open(csvname,encoding="utf-8") as csvfile:
        message_reader = csv.DictReader(csvfile)
        outname = csvpass + "one_message.csv"
        with open(outname, 'w',encoding="utf-8") as outfile:
            writer = csv.writer(outfile, lineterminator="\n")
            writer.writerow(('commitNo', 'message'))
            for row in message_reader:
                word = getwords(row["message"])
                if not word is None: 
                    writer.writerow((row["commitNo"], str(word)))
