import sys
import math
import treetaggerwrapper
from collections import Counter 
from operator import itemgetter

ARGV = sys.argv
ARGC = len(ARGV)

kindlist = ["e", "ee", "r", "rr", "o"]
if ARGC >= 2:
    txtlist = ["DepsR\\" + (ARGV[1]) + "\\" + x + "message.txt" for x in kindlist]
else:
    print("Usage: %s projectname" % ARGV[0])
    sys.exit()


tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='C:\TreeTagger')


print((ARGV[1]))
messages = [open(x, 'r', encoding = 'utf-8').read() for x in txtlist]

txt_num = len(messages)
  
fv_tf = []                      # ある文書中の単語の出現回数を格納するための配列
fv_df = {}                      # 単語の出現文書数を格納するためのディクショナリ
fv_df2 = Counter({})                      # 単語の出現回数を格納するためのディクショナリ
word_count = []                 # 単語の総出現回数を格納するための配列
  
fv_tf_idf = []                  # ある文書中の単語の特徴量を格納するための配列
  
count_flag = {}                 # fv_dfを計算する上で必要なフラグを格納するためのディクショナリ


# 各文書の形態素解析と、単語の出現回数の計算
for txt_id, txt in enumerate(messages):
    # MeCabを使うための初期化
    tags= treetaggerwrapper.make_tags(tagger.tag_text(txt), exclude_nottags=True)
    lemmas = [x.word for x in tags]

    fv = {}                     # 単語の出現回数を格納するためのディクショナリ
    words = 0                   # ある文書の単語の総出現回数
     
    for word in fv_df.keys():
        count_flag[word] = False

    for lemma in lemmas:
        surface = lemma # 形態素解析により得られた単語
  
        words += 1
  
        fv[surface] = fv.get(surface, 0) + 1 # fvにキー値がsurfaceの要素があれば、それに1を加え、なければ新しくキー値がsurfaceの要素をディクショナリに加え、値を1にする
  
        if surface in fv_df.keys(): # fv_dfにキー値がsurfaceの要素があれば
            if count_flag[surface] == False: # フラグを確認し，Falseであれば
                fv_df[surface] += 1 # 出現文書数を1増やす
                count_flag[surface] = True # フラグをTrueにする
        else:                 # fv_dfにキー値がsurfaceの要素がなければ
            fv_df[surface] = 1 # 新たにキー値がsurfaceの要素を作り，値として1を代入する
            count_flag[surface] = True # フラグをTrueにする
    
    fv_df2 = fv_df2 + Counter(fv)
    fv_tf.append(fv)
    word_count.append(words)

fv_df2 = dict(fv_df2)
  
# tf, idf, tf-idfなどの計算
for txt_id, fv in enumerate(fv_tf):
    tf = {}
    idf2 = {}
    idf = {}
    tf_idf = {}
    for key in fv.keys():
        tf[key] = float(fv[key]) / word_count[txt_id] # tfの計算
        idf[key] = math.log(float(txt_num) / fv_df[key]) # idfの計算
        idf2[key] = float(fv[key]) / fv_df2[key] # tfの計算
        

        tf_idf[key] = (tf[key]* idf2[key], tf[key] * idf[key], tf[key], idf[key], fv[key], fv_df[key]) # tf-idfその他の計算
    tf_idf = sorted(tf_idf.items(), key=lambda x:(x[1][1],x[1][0]), reverse=True) # 得られたディクショナリtf-idfを、tf[key]*idf[key](tf-idf値)で降順ソート(処理後にはtf-idfはリストオブジェクトになっている)
    fv_tf_idf.append(tf_idf)
  
# 出力

print(kindlist)

for id in range(0,10):
    for fv in fv_tf_idf:
        print(fv[id][0], end='')
        for i in range(0, (16 - len(fv[id][0]))):
            print(' ', end='')
        print('',end=',')
    print('')


#for txt_id, fv in enumerate(fv_tf_idf):
#    print('\n')
#    print('This is the tf-idf of text', txt_id)
#    print('total words:', word_count[txt_id])
#    print(kindlist[txt_id])
#    print("")
#    for id, (word, tf_idf) in enumerate(fv):
#        if(id > 10):
#            break
#        print('%s\toriginal:%lf\ttf-idf:%lf\ttf:%lf\tidf:%lf\tterm_count:%d\tdocument_count:%d' % (word, tf_idf[0], tf_idf[1], tf_idf[2], tf_idf[3], tf_idf[4], tf_idf[5])) # 左から順に、単語、original, tf-idf値、tf値、idf値、その文書中の単語の出現回数、その単語の出現文書数(これは単語ごとに同じ値をとる)