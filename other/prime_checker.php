<?php
/**
 * 素数判定プログラム（PHP版）
 */

/**
 * 素数判定を行う関数
 * @param int $n 判定したい正の整数
 * @return bool 素数の場合true、そうでなければfalse
 */
function isPrime($n) {
    if ($n < 2) return false;
    if ($n == 2) return true;
    if ($n % 2 == 0) return false;
    
    // 3から√nまでの奇数で割り切れるかチェック
    for ($i = 3; $i <= sqrt($n); $i += 2) {
        if ($n % $i == 0) return false;
    }
    return true;
}

/**
 * 数値を処理する関数
 * @param int $number 処理する数値
 */
function processNumber($number) {
    if ($number <= 0) {
        echo "エラー: 正の整数を入力してください\n";
        return;
    }
    
    if ($number > 10000000) {
        echo "エラー: 10,000,000以下の数値を入力してください\n";
        return;
    }
    
    if (isPrime($number)) {
        echo "{$number} は素数です\n";
    } else {
        echo "{$number} は素数ではありません\n";
    }
}

// メイン処理
try {
    if ($argc > 1) {
        // コマンドライン引数から取得
        $number = intval($argv[1]);
        if ($number == 0 && $argv[1] !== "0") {
            throw new InvalidArgumentException("無効な数値");
        }
    } else {
        // ユーザー入力から取得
        echo "判定したい数値を入力してください: ";
        $input = trim(fgets(STDIN));
        $number = intval($input);
        if ($number == 0 && $input !== "0") {
            throw new InvalidArgumentException("無効な数値");
        }
    }
    
    processNumber($number);
    
} catch (Exception $e) {
    echo "エラー: 有効な整数を入力してください\n";
}
?>