# DepsR
## makeSub
  * Doxydepsで生成したCSVに変更時間間隔を加えたCSVを出力
  * 生成されるファイルは `project_name.csv`から
    ```{r}
    project_name/root.csv
    project_name/deps.csv
    ```
## KindBoxPlot
  * makeSubで生成した`deps.csv`の変更時間間隔を箱ひげ図で出力

## CCoupling
  * `roots.csv`からコードカップリングを生成

## CCvsCIA
  * 変更時間間隔とCCouplingを比較
  * スピアマンの順位相関を利用

## CIA_estimate
  * 変更時間間隔での線形回帰を利用する