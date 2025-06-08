#!/usr/bin/env python3
import sys
import math

def is_prime(n):
    """
    素数判定を行う関数
    Args:
        n (int): 判定したい正の整数
    Returns:
        bool: 素数の場合True、そうでなければFalse
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 3から√nまでの奇数で割り切れるかチェック
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    try:
        if len(sys.argv) > 1:
            # コマンドライン引数から取得
            number = int(sys.argv[1])
        else:
            # ユーザー入力から取得
            number = int(input("判定したい数値を入力してください: "))
        
        if number <= 0:
            print("エラー: 正の整数を入力してください")
            return
        
        if number > 10000000:
            print("エラー: 10,000,000以下の数値を入力してください")
            return
        
        if is_prime(number):
            print(f"{number} は素数です")
        else:
            print(f"{number} は素数ではありません")
            
    except ValueError:
        print("エラー: 有効な整数を入力してください")
    except KeyboardInterrupt:
        print("\n処理が中断されました")

if __name__ == "__main__":
    main()