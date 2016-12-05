import sys
import csv
from git import Repo
import treetaggerwrapper

ARGV = sys.argv
ARGC = len(ARGV)

if ARGC == 4:
    REPO_PASS =  (ARGV[2]) + (ARGV[1]) # �t�@�C���p�X
    CSV_PASS = (ARGV[1]) + "message.csv"
    BRANCH_NAME = (ARGV[3])
else:
    print("Usage: %s repopass csvpass master_branch_name" % ARGV[0])
    sys.exit()

REPO = Repo(REPO_PASS)

COMMITS_LEN = len(list(REPO.iter_commits(BRANCH_NAME)))


WRITER = csv.writer(open(CSV_PASS, "w", encoding="utf-8"), lineterminator="\n")
tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='C:\TreeTagger')

for commit_no, item in enumerate(REPO.iter_commits(BRANCH_NAME)):
    
    commitmessage = item.message.replace('\n','')


    #tags = treetaggerwrapper.make_tags(tagger.tag_text(commitmessage), exclude_nottags=True)
    #clemma = [x.lemma for x in tags]
    #print(clemma)
    WRITER.writerow((commit_no, commitmessage))
