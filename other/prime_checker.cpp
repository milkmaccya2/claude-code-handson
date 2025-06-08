#include <iostream>
#include <cmath>
#include <string>

/**
 * 素数判定を行う関数
 * @param n 判定したい正の整数
 * @return 素数の場合true、そうでなければfalse
 */
bool isPrime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    
    // 3から√nまでの奇数で割り切れるかチェック
    for (int i = 3; i <= std::sqrt(n); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

/**
 * 数値を処理する関数
 * @param number 処理する数値
 */
void processNumber(int number) {
    if (number <= 0) {
        std::cout << "エラー: 正の整数を入力してください" << std::endl;
        return;
    }
    
    if (number > 10000000) {
        std::cout << "エラー: 10,000,000以下の数値を入力してください" << std::endl;
        return;
    }
    
    if (isPrime(number)) {
        std::cout << number << " は素数です" << std::endl;
    } else {
        std::cout << number << " は素数ではありません" << std::endl;
    }
}

int main(int argc, char* argv[]) {
    try {
        int number;
        
        if (argc > 1) {
            // コマンドライン引数から取得
            number = std::stoi(argv[1]);
        } else {
            // ユーザー入力から取得
            std::cout << "判定したい数値を入力してください: ";
            std::cin >> number;
            
            if (std::cin.fail()) {
                std::cout << "エラー: 有効な整数を入力してください" << std::endl;
                return 1;
            }
        }
        
        processNumber(number);
        
    } catch (const std::invalid_argument& e) {
        std::cout << "エラー: 有効な整数を入力してください" << std::endl;
        return 1;
    } catch (const std::out_of_range& e) {
        std::cout << "エラー: 数値が範囲外です" << std::endl;
        return 1;
    } catch (const std::exception& e) {
        std::cout << "エラー: 処理中に問題が発生しました" << std::endl;
        return 1;
    }
    
    return 0;
}