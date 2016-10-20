# Doxydeps

２つのプロジェクトを用意

## Doxydeps
* doxygenから依存関係を出力
* python3を利用
### 実行方法
`python3 Doxydeps.py 依存関係元ファイルパス 出力先　調査するブランチ名(master)`



## DepsR
### makeSub
* Doxydepsで生成したCSVに変更時間間隔を加えたCSVを出力
* 生成されるファイルは `project_name.csv`から
`project_name/root.csv`,`project_name/deps.csv`
### KindBoxPlot
* makeSubで生成した`deps.csv`の変更時間間隔を箱ひげ図で出力
### CCoupling
* `roots.csv`からコードカップリングを生成
### CCvsCIA
* 変更時間間隔とCCouplingを比較