# Doxydeps(Doxygen for dependency)
依存関係を出力するプログラム
## Doxydeps
doxygenから全コミットの依存関係を出力

### 内容
* doxygenから依存関係を出力
* python3を利用

### 実行方法
```{r}
python3 Doxydeps.py 調査対象プロジェクトファイルパス 出力先　調査するブランチ名(master)
```

### 出力結果
太字は主キー

**`commitNo`**, **`file_location`**, `date`, `author`, `is_merge`, **`kind`**

### 必要環境
* git
* python3
* gitpython
* Doxygen(実行パスを通しておく必要がある)

### 構成
* Doxydeps.py
* GetDeps内のファイル

## GitLines.py
Gitで追加された行数と削除された行数を出力する

### 実行方法
`python3 リポジトリパス 出力先フォルダ 調査するブランチ名(master)`

### 出力結果
太字は主キー

**`commit_no`**, **`file_path`**, `deletions`, `insertions`, `lines`

**コミット番号**,**ファイルパス**,削除行数,挿入行数,合計行

## GitTagger.py

## NaiveBaysian.py

## Double_NaiveBaysian.py_