#!/usr/bin/env runhaskell
import System.Environment (getArgs)
import System.IO (hFlush, stdout)
import Text.Read (readMaybe)

-- 素数判定を行う関数
-- n: 判定したい正の整数
-- 戻り値: 素数の場合True、そうでなければFalse
isPrime :: Int -> Bool
isPrime n
    | n < 2 = False
    | n == 2 = True
    | even n = False
    | otherwise = not $ any (\x -> n `mod` x == 0) [3, 5 .. floor $ sqrt $ fromIntegral n]

-- 数値を処理する関数
-- number: 処理する数値
processNumber :: Int -> IO ()
processNumber number
    | number <= 0 = putStrLn "エラー: 正の整数を入力してください"
    | number > 10000000 = putStrLn "エラー: 10,000,000以下の数値を入力してください"
    | isPrime number = putStrLn $ show number ++ " は素数です"
    | otherwise = putStrLn $ show number ++ " は素数ではありません"

-- 文字列を整数に変換する安全な関数
safeRead :: String -> Maybe Int
safeRead = readMaybe

-- ユーザー入力を取得する関数
getUserInput :: IO (Maybe Int)
getUserInput = do
    putStr "判定したい数値を入力してください: "
    hFlush stdout
    input <- getLine
    return $ safeRead input

-- メイン処理
main :: IO ()
main = do
    args <- getArgs
    maybeNumber <- case args of
        [] -> getUserInput  -- ユーザー入力から取得
        (arg:_) -> return $ safeRead arg  -- コマンドライン引数から取得
    
    case maybeNumber of
        Just number -> processNumber number
        Nothing -> putStrLn "エラー: 有効な整数を入力してください"