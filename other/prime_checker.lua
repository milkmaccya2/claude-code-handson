#!/usr/bin/env lua

-- 素数判定を行う関数
-- @param n 判定したい正の整数
-- @return 素数の場合true、そうでなければfalse
function isPrime(n)
    if n < 2 then return false end
    if n == 2 then return true end
    if n % 2 == 0 then return false end
    
    -- 3から√nまでの奇数で割り切れるかチェック
    local sqrt_n = math.floor(math.sqrt(n))
    for i = 3, sqrt_n, 2 do
        if n % i == 0 then return false end
    end
    return true
end

-- 数値を処理する関数
-- @param number 処理する数値
function processNumber(number)
    if number <= 0 then
        print("エラー: 正の整数を入力してください")
        return
    end
    
    if number > 10000000 then
        print("エラー: 10,000,000以下の数値を入力してください")
        return
    end
    
    if isPrime(number) then
        print(number .. " は素数です")
    else
        print(number .. " は素数ではありません")
    end
end

-- メイン処理
function main()
    local number
    
    if arg and arg[1] then
        -- コマンドライン引数から取得
        number = tonumber(arg[1])
        if not number then
            print("エラー: 有効な整数を入力してください")
            os.exit(1)
        end
    else
        -- ユーザー入力から取得
        io.write("判定したい数値を入力してください: ")
        local input = io.read()
        number = tonumber(input)
        if not number then
            print("エラー: 有効な整数を入力してください")
            os.exit(1)
        end
    end
    
    processNumber(math.floor(number))
end

-- プログラム実行
main()