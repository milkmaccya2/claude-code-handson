import java.util.Scanner;

/**
 * 素数判定プログラム（Java版）
 */
public class PrimeChecker {
    
    /**
     * 素数判定を行うメソッド
     * @param n 判定したい正の整数
     * @return 素数の場合true、そうでなければfalse
     */
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        
        // 3から√nまでの奇数で割り切れるかチェック
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    /**
     * 数値を処理するメソッド
     * @param number 処理する数値
     */
    public static void processNumber(int number) {
        if (number <= 0) {
            System.out.println("エラー: 正の整数を入力してください");
            return;
        }
        
        if (number > 10000000) {
            System.out.println("エラー: 10,000,000以下の数値を入力してください");
            return;
        }
        
        if (isPrime(number)) {
            System.out.println(number + " は素数です");
        } else {
            System.out.println(number + " は素数ではありません");
        }
    }
    
    public static void main(String[] args) {
        try {
            int number;
            
            if (args.length > 0) {
                // コマンドライン引数から取得
                number = Integer.parseInt(args[0]);
            } else {
                // ユーザー入力から取得
                Scanner scanner = new Scanner(System.in);
                System.out.print("判定したい数値を入力してください: ");
                number = scanner.nextInt();
                scanner.close();
            }
            
            processNumber(number);
            
        } catch (NumberFormatException e) {
            System.out.println("エラー: 有効な整数を入力してください");
        } catch (Exception e) {
            System.out.println("エラー: 処理中に問題が発生しました");
        }
    }
}