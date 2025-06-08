use std::env;
use std::io;

/// 素数判定を行う関数
fn is_prime(n: u32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }

    // 3から√nまでの奇数で割り切れるかチェック
    let sqrt = (n as f64).sqrt() as u32;
    for i in (3..=sqrt).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    true
}

/// 数値を処理する関数
fn process_number(number: u32) {
    if number == 0 {
        println!("エラー: 正の整数を入力してください");
        return;
    }

    if number > 10_000_000 {
        println!("エラー: 10,000,000以下の数値を入力してください");
        return;
    }

    if is_prime(number) {
        println!("{} は素数です", number);
    } else {
        println!("{} は素数ではありません", number);
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let number: u32;

    if args.len() > 1 {
        // コマンドライン引数から取得
        match args[1].parse() {
            Ok(n) => number = n,
            Err(_) => {
                println!("エラー: 有効な整数を入力してください");
                return;
            }
        }
    } else {
        // ユーザー入力から取得
        println!("判定したい数値を入力してください: ");
        let mut input = String::new();
        
        match io::stdin().read_line(&mut input) {
            Ok(_) => {
                match input.trim().parse() {
                    Ok(n) => number = n,
                    Err(_) => {
                        println!("エラー: 有効な整数を入力してください");
                        return;
                    }
                }
            }
            Err(_) => {
                println!("エラー: 入力の読み取りに失敗しました");
                return;
            }
        }
    }

    process_number(number);
}