using System;

/// <summary>
/// 素数判定プログラム（C#版）
/// </summary>
class PrimeChecker
{
    /// <summary>
    /// 素数判定を行うメソッド
    /// </summary>
    /// <param name="n">判定したい正の整数</param>
    /// <returns>素数の場合true、そうでなければfalse</returns>
    static bool IsPrime(int n)
    {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        // 3から√nまでの奇数で割り切れるかチェック
        for (int i = 3; i <= Math.Sqrt(n); i += 2)
        {
            if (n % i == 0) return false;
        }
        return true;
    }

    /// <summary>
    /// 数値を処理するメソッド
    /// </summary>
    /// <param name="number">処理する数値</param>
    static void ProcessNumber(int number)
    {
        if (number <= 0)
        {
            Console.WriteLine("エラー: 正の整数を入力してください");
            return;
        }

        if (number > 10000000)
        {
            Console.WriteLine("エラー: 10,000,000以下の数値を入力してください");
            return;
        }

        if (IsPrime(number))
        {
            Console.WriteLine($"{number} は素数です");
        }
        else
        {
            Console.WriteLine($"{number} は素数ではありません");
        }
    }

    static void Main(string[] args)
    {
        try
        {
            int number;

            if (args.Length > 0)
            {
                // コマンドライン引数から取得
                number = int.Parse(args[0]);
            }
            else
            {
                // ユーザー入力から取得
                Console.Write("判定したい数値を入力してください: ");
                string input = Console.ReadLine();
                number = int.Parse(input);
            }

            ProcessNumber(number);
        }
        catch (FormatException)
        {
            Console.WriteLine("エラー: 有効な整数を入力してください");
        }
        catch (OverflowException)
        {
            Console.WriteLine("エラー: 数値が範囲外です");
        }
        catch (Exception)
        {
            Console.WriteLine("エラー: 処理中に問題が発生しました");
        }
    }
}