import Foundation

/**
 * 素数判定を行う関数
 * - Parameter n: 判定したい正の整数
 * - Returns: 素数の場合true、そうでなければfalse
 */
func isPrime(_ n: Int) -> Bool {
    if n < 2 { return false }
    if n == 2 { return true }
    if n % 2 == 0 { return false }
    
    // 3から√nまでの奇数で割り切れるかチェック
    let sqrt = Int(Double(n).squareRoot())
    for i in stride(from: 3, through: sqrt, by: 2) {
        if n % i == 0 { return false }
    }
    return true
}

/**
 * 数値を処理する関数
 * - Parameter number: 処理する数値
 */
func processNumber(_ number: Int) {
    if number <= 0 {
        print("エラー: 正の整数を入力してください")
        return
    }
    
    if number > 10_000_000 {
        print("エラー: 10,000,000以下の数値を入力してください")
        return
    }
    
    if isPrime(number) {
        print("\(number) は素数です")
    } else {
        print("\(number) は素数ではありません")
    }
}

// メイン処理
func main() {
    let arguments = CommandLine.arguments
    
    do {
        let number: Int
        
        if arguments.count > 1 {
            // コマンドライン引数から取得
            guard let num = Int(arguments[1]) else {
                throw NSError(domain: "InvalidInput", code: 1, userInfo: nil)
            }
            number = num
        } else {
            // ユーザー入力から取得
            print("判定したい数値を入力してください: ", terminator: "")
            guard let input = readLine(), let num = Int(input) else {
                throw NSError(domain: "InvalidInput", code: 1, userInfo: nil)
            }
            number = num
        }
        
        processNumber(number)
        
    } catch {
        print("エラー: 有効な整数を入力してください")
    }
}

// プログラム実行
main()