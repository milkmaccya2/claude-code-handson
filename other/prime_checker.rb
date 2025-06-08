#!/usr/bin/env ruby

# 素数判定を行う関数
# @param n [Integer] 判定したい正の整数
# @return [Boolean] 素数の場合true、そうでなければfalse
def prime?(n)
  return false if n < 2
  return true if n == 2
  return false if n.even?
  
  # 3から√nまでの奇数で割り切れるかチェック
  (3..Math.sqrt(n)).step(2) do |i|
    return false if n % i == 0
  end
  true
end

# 数値を処理する関数
# @param number [Integer] 処理する数値
def process_number(number)
  if number <= 0
    puts "エラー: 正の整数を入力してください"
    return
  end
  
  if number > 10_000_000
    puts "エラー: 10,000,000以下の数値を入力してください"
    return
  end
  
  if prime?(number)
    puts "#{number} は素数です"
  else
    puts "#{number} は素数ではありません"
  end
end

# メイン処理
begin
  if ARGV.length > 0
    # コマンドライン引数から取得
    number = Integer(ARGV[0])
  else
    # ユーザー入力から取得
    print "判定したい数値を入力してください: "
    input = gets.chomp
    number = Integer(input)
  end
  
  process_number(number)
  
rescue ArgumentError
  puts "エラー: 有効な整数を入力してください"
rescue StandardError => e
  puts "エラー: 処理中に問題が発生しました"
end