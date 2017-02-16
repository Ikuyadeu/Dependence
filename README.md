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

### 必要環境
* git
* python3
* gitpython
* Doxygen(実行パスを通しておく必要がある)

### 構成
* Doxydeps.py
* GetDeps内のファイル