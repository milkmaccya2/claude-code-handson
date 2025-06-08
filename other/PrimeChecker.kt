import kotlin.math.sqrt

/**
 * 素数判定プログラム（Kotlin版）
 */
object PrimeChecker {
    
    /**
     * 素数判定を行う関数
     * @param n 判定したい正の整数
     * @return 素数の場合true、そうでなければfalse
     */
    fun isPrime(n: Int): Boolean {
        if (n < 2) return false
        if (n == 2) return true
        if (n % 2 == 0) return false
        
        // 3から√nまでの奇数で割り切れるかチェック
        for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
            if (n % i == 0) return false
        }
        return true
    }
    
    /**
     * 数値を処理する関数
     * @param number 処理する数値
     */
    fun processNumber(number: Int) {
        when {
            number <= 0 -> {
                println("エラー: 正の整数を入力してください")
                return
            }
            number > 10_000_000 -> {
                println("エラー: 10,000,000以下の数値を入力してください")
                return
            }
            isPrime(number) -> {
                println("$number は素数です")
            }
            else -> {
                println("$number は素数ではありません")
            }
        }
    }
    
    @JvmStatic
    fun main(args: Array<String>) {
        try {
            val number = when {
                args.isNotEmpty() -> {
                    // コマンドライン引数から取得
                    args[0].toInt()
                }
                else -> {
                    // ユーザー入力から取得
                    print("判定したい数値を入力してください: ")
                    readLine()?.toInt() ?: throw NumberFormatException("無効な入力")
                }
            }
            
            processNumber(number)
            
        } catch (e: NumberFormatException) {
            println("エラー: 有効な整数を入力してください")
        } catch (e: Exception) {
            println("エラー: 処理中に問題が発生しました")
        }
    }
}