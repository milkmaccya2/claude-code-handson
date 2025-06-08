#!/usr/bin/env node

/**
 * 素数判定を行う関数
 * @param {number} n - 判定したい正の整数
 * @returns {boolean} 素数の場合true、そうでなければfalse
 */
function isPrime(n) {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    
    // 3から√nまでの奇数で割り切れるかチェック
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        if (n % i === 0) return false;
    }
    return true;
}

function main() {
    let number;
    
    try {
        if (process.argv.length > 2) {
            // コマンドライン引数から取得
            number = parseInt(process.argv[2]);
        } else {
            // Node.js環境でのユーザー入力
            const readline = require('readline');
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            });
            
            rl.question('判定したい数値を入力してください: ', (input) => {
                try {
                    number = parseInt(input);
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

function processNumber(number) {
    if (isNaN(number) || number <= 0) {
        console.log('エラー: 正の整数を入力してください');
        return;
    }
    
    if (number > 10000000) {
        console.log('エラー: 10,000,000以下の数値を入力してください');
        return;
    }
    
    if (isPrime(number)) {
        console.log(`${number} は素数です`);
    } else {
        console.log(`${number} は素数ではありません`);
    }
}

// ブラウザ環境とNode.js環境の両方に対応
if (typeof window === 'undefined') {
    // Node.js環境
    main();
} else {
    // ブラウザ環境
    window.isPrime = isPrime;
    window.processNumber = processNumber;
}