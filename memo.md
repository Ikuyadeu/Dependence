# 研究メモ
## 現在利用されているレビュアー推薦ボット
* [mention-bot](https://github.com/facebook/mention-bot)(javascript):facebook製.git blameから過去を遡ってレビュアーを選定する
* hobbit-bot:ランダムにレビュアーを選定する

## 利用できそうな技術(** 太字 **は利用テスト中)
* タグ付け:ctags, ** gtags **
* 呼び出し関係:ctrace, Itrace, strace, ktrace, trusss
* 依存関係を調べるもの:** [Doxygen](http://www.doxygen.jp/)(ドキシジェン) **, Understand

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

## gtagsを利用するにあたって
* 調べる際にはファイルごとということができるのでそれを利用する.
* HTML形式で出力するのでXMLで出力・解析する方法を調べたい.
* 調査可能言語:C, C++, Yacc, Java, PHP4(他にもあるにはあるがいまいちリンクしてない)
* 使い方が日本語で書いてあった！http://www.machu.jp/diary/20090307.html
* XML形式が使えないのが不安

## doxygenを利用するにあたって
* XML形式で出力可能！
* ファイル名がわかりやすいので処理が簡単そう
* GUIで動かしているからコマンドを利用した自動化ができるかどうかが不安
* 使い方 http://www.doxygen.jp/manual.html

```
# 設定ファイルを作成する
doxygen -g <config_file>
```