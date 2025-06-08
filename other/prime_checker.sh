#!/bin/bash

# 素数判定を行う関数
# 引数: $1 - 判定したい正の整数
# 戻り値: 素数の場合0、そうでなければ1
is_prime() {
    local n=$1
    
    if [ $n -lt 2 ]; then
        return 1
    fi
    
    if [ $n -eq 2 ]; then
        return 0
    fi
    
    if [ $((n % 2)) -eq 0 ]; then
        return 1
    fi
    
    # 3から√nまでの奇数で割り切れるかチェック
    local sqrt_n=$(echo "sqrt($n)" | bc -l | cut -d. -f1)
    for ((i=3; i<=sqrt_n; i+=2)); do
        if [ $((n % i)) -eq 0 ]; then
            return 1
        fi
    done
    
    return 0
}

# 数値を処理する関数
# 引数: $1 - 処理する数値
process_number() {
    local number=$1
    
    if [ $number -le 0 ]; then
        echo "エラー: 正の整数を入力してください"
        return
    fi
    
    if [ $number -gt 10000000 ]; then
        echo "エラー: 10,000,000以下の数値を入力してください"
        return
    fi
    
    if is_prime $number; then
        echo "$number は素数です"
    else
        echo "$number は素数ではありません"
    fi
}

# 数値が整数かチェックする関数
is_integer() {
    [[ $1 =~ ^[0-9]+$ ]]
}

# メイン処理
main() {
    local number
    
    if [ $# -gt 0 ]; then
        # コマンドライン引数から取得
        number=$1
    else
        # ユーザー入力から取得
        read -p "判定したい数値を入力してください: " number
    fi
    
    if ! is_integer "$number"; then
        echo "エラー: 有効な整数を入力してください"
        exit 1
    fi
    
    process_number $number
}

# bcコマンドの存在確認
if ! command -v bc &> /dev/null; then
    echo "エラー: bcコマンドが必要です"
    exit 1
fi

# プログラム実行
main "$@"