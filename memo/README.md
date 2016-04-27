# 研究メモ
## 現在利用されているレビュアー推薦ボット
* [mention-bot](https://github.com/facebook/mention-bot)(javascript):facebook製.git blameから過去を遡ってレビュアーを選定する
* hobbit-bot:ランダムにレビュアーを選定する

## 利用できそうな技術
* タグ付け:ctags, gtags
* 呼び出し関係:ctrace, Itrace, strace, ktrace, trusss
* 依存関係を調べるもの:** [Doxygen](http://www.doxygen.jp/) **, Understand

## 提案手法の評価基準
### 長さ
* 時間
* レビュー数  

### レビュー後の行動
* リピート率

### 人数
* 推薦される人数
* 一人当たりの担当数  
  max down, mid up　となればいい感じにばらついている感じがする

### 信頼性
* ~~無理かも~~
* 妥協案: 最終状態がmergeかcloseか(not open)
mergeなら最終的に使えるものにしたということになる


## 名前（仮)
* territory-bot(レビュアーの得意領域を依存関係から定義する)

## Doxygen採用にあたって
* Doxygenをコマンドラインから実行する方法を探す必要がある.
* 調べる際にはファイルごとということができるのでそれを利用する.
* HTML, XML形式で出力するのでXMLを解析する方法を調べたい.