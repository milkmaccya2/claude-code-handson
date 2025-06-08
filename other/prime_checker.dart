import 'dart:io';
import 'dart:math';

/// 素数判定を行う関数
/// [n] 判定したい正の整数
/// 戻り値: 素数の場合true、そうでなければfalse
bool isPrime(int n) {
  if (n < 2) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;
  
  // 3から√nまでの奇数で割り切れるかチェック
  int sqrtN = sqrt(n).toInt();
  for (int i = 3; i <= sqrtN; i += 2) {
    if (n % i == 0) return false;
  }
  return true;
}

/// 数値を処理する関数
/// [number] 処理する数値
void processNumber(int number) {
  if (number <= 0) {
    print('エラー: 正の整数を入力してください');
    return;
  }
  
  if (number > 10000000) {
    print('エラー: 10,000,000以下の数値を入力してください');
    return;
  }
  
  if (isPrime(number)) {
    print('$number は素数です');
  } else {
    print('$number は素数ではありません');
  }
}

void main(List<String> args) async {
  int? number;
  
  try {
    if (args.isNotEmpty) {
      // コマンドライン引数から取得
      number = int.parse(args[0]);
    } else {
      // ユーザー入力から取得
      stdout.write('判定したい数値を入力してください: ');
      String? input = stdin.readLineSync();
      if (input != null) {
        number = int.parse(input);
      }
    }
    
    if (number != null) {
      processNumber(number);
    } else {
      print('エラー: 有効な整数を入力してください');
    }
    
  } catch (e) {
    print('エラー: 有効な整数を入力してください');
  }
}