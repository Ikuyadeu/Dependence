/**
 * @file Doc.h
 * @brief ここに要約文を記述します。<br>
 *        むにゃむにゃむにゃむにゃむにゃむにゃ。
 * @author 作者の名前を書きます
 * @date 年が明けた日<br>
 *       作成着手
 * @date 次の日<br>
 *       完成したＹＯ！
 */

namespace myNamespace {
        /**
         * クラス説明の要約をここに書く。<br>
         * むにゃむにゃむにゃ.
         */
        class Doc {
        public:
                /** デフォルトコンストラクタ. */
                Doc() {}
                /**
                 * コンストラクタ.
                 * @param num 回数を指定する(引数の説明)
                 */
                Doc(int num) { 
                        this->num = num;
                }
                /**
                 * コピーコンストラクタ.
                 * @param doc コピー元オブジェクト
                 */
                Doc(Doc& doc) {
                        setNum(doc.getNum());
                }
                /** ディストラクタ. */
                virtual ~Doc() {}

                /** ANIMALの説明だよん */
                enum ANIMAL {
                        /** 猫. */
                        CAT,
                        /** 犬. */
                        DOG,
                        /** 鳥. */
                        BIRD
                };

                /**
                 * メンバ関数のコメント.
                 * @return ループ処理を行った回数(戻り値の説明)
                 */
                int doWork();

                /** @return 内部で保持している番号 **/
                int getNum() const { return num; }
                /** @param num 番号 */
                void setNum(int num) { this->num = num; }
        private:
                /** 内部で保持している番号（メンバ変数へのコメント） */
                int num;
        };
}