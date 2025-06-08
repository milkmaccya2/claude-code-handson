import scala.io.StdIn
import scala.util.{Try, Success, Failure}

object PrimeChecker {
  
  /**
   * 素数判定を行う関数
   * @param n 判定したい正の整数
   * @return 素数の場合true、そうでなければfalse
   */
  def isPrime(n: Int): Boolean = {
    if (n < 2) false
    else if (n == 2) true
    else if (n % 2 == 0) false
    else {
      // 3から√nまでの奇数で割り切れるかチェック
      val sqrt = math.sqrt(n).toInt
      (3 to sqrt by 2).forall(n % _ != 0)
    }
  }
  
  /**
   * 数値を処理する関数
   * @param number 処理する数値
   */
  def processNumber(number: Int): Unit = {
    number match {
      case n if n <= 0 =>
        println("エラー: 正の整数を入力してください")
      case n if n > 10000000 =>
        println("エラー: 10,000,000以下の数値を入力してください")
      case n if isPrime(n) =>
        println(s"$n は素数です")
      case n =>
        println(s"$n は素数ではありません")
    }
  }
  
  def main(args: Array[String]): Unit = {
    val numberOpt = if (args.nonEmpty) {
      // コマンドライン引数から取得
      Try(args(0).toInt).toOption
    } else {
      // ユーザー入力から取得
      print("判定したい数値を入力してください: ")
      Try(StdIn.readInt()).toOption
    }
    
    numberOpt match {
      case Some(number) => processNumber(number)
      case None => println("エラー: 有効な整数を入力してください")
    }
  }
}