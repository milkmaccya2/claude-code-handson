package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

// isPrime 素数判定を行う関数
func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}

	// 3から√nまでの奇数で割り切れるかチェック
	sqrt := int(math.Sqrt(float64(n)))
	for i := 3; i <= sqrt; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// processNumber 数値を処理する関数
func processNumber(number int) {
	if number <= 0 {
		fmt.Println("エラー: 正の整数を入力してください")
		return
	}

	if number > 10000000 {
		fmt.Println("エラー: 10,000,000以下の数値を入力してください")
		return
	}

	if isPrime(number) {
		fmt.Printf("%d は素数です\n", number)
	} else {
		fmt.Printf("%d は素数ではありません\n", number)
	}
}

func main() {
	var number int
	var err error

	if len(os.Args) > 1 {
		// コマンドライン引数から取得
		number, err = strconv.Atoi(os.Args[1])
		if err != nil {
			fmt.Println("エラー: 有効な整数を入力してください")
			os.Exit(1)
		}
	} else {
		// ユーザー入力から取得
		fmt.Print("判定したい数値を入力してください: ")
		_, err = fmt.Scanf("%d", &number)
		if err != nil {
			fmt.Println("エラー: 有効な整数を入力してください")
			os.Exit(1)
		}
	}

	processNumber(number)
}