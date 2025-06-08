#!/usr/bin/env Rscript

# 素数判定を行う関数
# @param n 判定したい正の整数
# @return 素数の場合TRUE、そうでなければFALSE
is_prime <- function(n) {
  if (n < 2) return(FALSE)
  if (n == 2) return(TRUE)
  if (n %% 2 == 0) return(FALSE)
  
  # 3から√nまでの奇数で割り切れるかチェック
  sqrt_n <- floor(sqrt(n))
  for (i in seq(3, sqrt_n, by = 2)) {
    if (n %% i == 0) return(FALSE)
  }
  return(TRUE)
}

# 数値を処理する関数
# @param number 処理する数値
process_number <- function(number) {
  if (number <= 0) {
    cat("エラー: 正の整数を入力してください\n")
    return()
  }
  
  if (number > 10000000) {
    cat("エラー: 10,000,000以下の数値を入力してください\n")
    return()
  }
  
  if (is_prime(number)) {
    cat(number, "は素数です\n")
  } else {
    cat(number, "は素数ではありません\n")
  }
}

# メイン処理
main <- function() {
  args <- commandArgs(trailingOnly = TRUE)
  
  tryCatch({
    if (length(args) > 0) {
      # コマンドライン引数から取得
      number <- as.integer(args[1])
      if (is.na(number)) {
        stop("Invalid number")
      }
    } else {
      # ユーザー入力から取得
      cat("判定したい数値を入力してください: ")
      input <- readLines(con = "stdin", n = 1)
      number <- as.integer(input)
      if (is.na(number)) {
        stop("Invalid number")
      }
    }
    
    process_number(number)
    
  }, error = function(e) {
    cat("エラー: 有効な整数を入力してください\n")
  })
}

# プログラム実行
if (!interactive()) {
  main()
}