#!/usr/bin/env ts-node

/**
 * 素数判定を行う関数
 * @param n - 判定したい正の整数
 * @returns 素数の場合true、そうでなければfalse
 */
function isPrime(n: number): boolean {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    
    // 3から√nまでの奇数で割り切れるかチェック
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        if (n % i === 0) return false;
    }
    return true;
}

/**
 * 数値を処理する関数
 * @param number - 処理する数値
 */
function processNumber(number: number): void {
    if (number <= 0) {
        console.log('エラー: 正の整数を入力してください');
        return;
    }
    
    if (number > 10_000_000) {
        console.log('エラー: 10,000,000以下の数値を入力してください');
        return;
    }
    
    if (isPrime(number)) {
        console.log(`${number} は素数です`);
    } else {
        console.log(`${number} は素数ではありません`);
    }
}

function main(): void {
    const args = process.argv.slice(2);
    let number: number;
    
    try {
        if (args.length > 0) {
            // コマンドライン引数から取得
            number = parseInt(args[0], 10);
            if (isNaN(number)) {
                throw new Error('Invalid number');
            }
        } else {
            // Node.js環境でのユーザー入力
            const readline = require('readline');
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            });
            
            rl.question('判定したい数値を入力してください: ', (input: string) => {
                try {
                    number = parseInt(input, 10);
                    if (isNaN(number)) {
                        throw new Error('Invalid number');
                    }
                    processNumber(number);
                } catch (error) {
                    console.log('エラー: 有効な整数を入力してください');
                }
                rl.close();
            });
            return;
        }
        
        processNumber(number);
        
    } catch (error) {
        console.log('エラー: 有効な整数を入力してください');
    }
}

// TypeScriptコンパイル後の実行環境判定
if (require.main === module) {
    main();
}

export { isPrime, processNumber };