#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

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
    int sqrt_n = (int)sqrt(n);
    for (int i = 3; i <= sqrt_n; i += 2) {
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
        printf("エラー: 正の整数を入力してください\n");
        return;
    }
    
    if (number > 10000000) {
        printf("エラー: 10,000,000以下の数値を入力してください\n");
        return;
    }
    
    if (isPrime(number)) {
        printf("%d は素数です\n", number);
    } else {
        printf("%d は素数ではありません\n", number);
    }
}

int main(int argc, char *argv[]) {
    int number;
    
    if (argc > 1) {
        // コマンドライン引数から取得
        char *endptr;
        number = strtol(argv[1], &endptr, 10);
        
        if (*endptr != '\0' || endptr == argv[1]) {
            printf("エラー: 有効な整数を入力してください\n");
            return 1;
        }
    } else {
        // ユーザー入力から取得
        printf("判定したい数値を入力してください: ");
        if (scanf("%d", &number) != 1) {
            printf("エラー: 有効な整数を入力してください\n");
            return 1;
        }
    }
    
    processNumber(number);
    return 0;
}