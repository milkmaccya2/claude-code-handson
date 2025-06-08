#!/usr/bin/env perl
use strict;
use warnings;
use POSIX qw(floor);

# 素数判定を行う関数
# 引数: $n - 判定したい正の整数
# 戻り値: 素数の場合1、そうでなければ0
sub is_prime {
    my ($n) = @_;
    return 0 if $n < 2;
    return 1 if $n == 2;
    return 0 if $n % 2 == 0;
    
    # 3から√nまでの奇数で割り切れるかチェック
    my $sqrt_n = floor(sqrt($n));
    for my $i (3..$sqrt_n) {
        next if $i % 2 == 0;  # 偶数をスキップ
        return 0 if $n % $i == 0;
    }
    return 1;
}

# 数値を処理する関数
# 引数: $number - 処理する数値
sub process_number {
    my ($number) = @_;
    
    if ($number <= 0) {
        print "エラー: 正の整数を入力してください\n";
        return;
    }
    
    if ($number > 10_000_000) {
        print "エラー: 10,000,000以下の数値を入力してください\n";
        return;
    }
    
    if (is_prime($number)) {
        print "$number は素数です\n";
    } else {
        print "$number は素数ではありません\n";
    }
}

# メイン処理
sub main {
    my $number;
    
    if (@ARGV > 0) {
        # コマンドライン引数から取得
        $number = $ARGV[0];
        unless ($number =~ /^\d+$/) {
            print "エラー: 有効な整数を入力してください\n";
            exit 1;
        }
    } else {
        # ユーザー入力から取得
        print "判定したい数値を入力してください: ";
        chomp($number = <STDIN>);
        unless ($number =~ /^\d+$/) {
            print "エラー: 有効な整数を入力してください\n";
            exit 1;
        }
    }
    
    process_number(int($number));
}

# プログラム実行
main() unless caller;