/**
 * @file main.cpp
 * @brief main関数を定義しています。<br>
 *        にゃんにゃん。
 *
 *        プログラムのエントリポイントを定義しています。<br>
 *        前後に空白行をいれて、詳細を記述します。
 * @par   これで1つのパラグラフを定義できます、
 *        詳細をわーーーーーーーーーーーーーーーーーーーーーー<br>
 *        っとここに記述します。
 * @par   複数定義できます。
 *        うひぃｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ<br>
 *        わんわんお♪
 * @date  2013/01/02 新規作成！
 * @date  同日 作成完了（dateだからといって日付を書く必要はない。）
 * @author 作者の名前を書きます
 */
#include "Doc.h"

/**
 * メイン処理.
 * @param argc 引数の数
 * @param argv 引数の値の配列
 * @return リターンコード
 */
int main(int argc, char** argv) {

        // 処理を実行する
        myNamespace::Doc obj(10);
        obj.doWork();

}