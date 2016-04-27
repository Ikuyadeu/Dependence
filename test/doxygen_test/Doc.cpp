/**
 * @file Doc.cpp
 * @brief Docクラスの実装
 * @author 作者の名前を書きます
 */

#include <iostream>
#include "Doc.h"

namespace myNamespace {
        /*
         * 仕事をします！.
         * @return 戻り値だお！
         */
        int Doc::doWork() {
                // 猫の鳴き声を出力
                int i;
                for (i=0; i<getNum(); i++) {
                        std::cout << "にゃん\n";
                }

                return i+1;
        }
} 