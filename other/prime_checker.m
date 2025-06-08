function prime_checker(varargin)
    % 素数判定プログラム（MATLAB版）
    % 使用方法: prime_checker() または prime_checker(number)
    
    if nargin > 0
        % 引数として数値が渡された場合
        number = varargin{1};
        if ~isnumeric(number) || ~isscalar(number) || number ~= floor(number)
            fprintf('エラー: 有効な整数を入力してください\n');
            return;
        end
    else
        % ユーザー入力から取得
        number = input('判定したい数値を入力してください: ');
        if ~isnumeric(number) || ~isscalar(number) || number ~= floor(number)
            fprintf('エラー: 有効な整数を入力してください\n');
            return;
        end
    end
    
    processNumber(number);
end

function result = isPrime(n)
    % 素数判定を行う関数
    % 入力: n - 判定したい正の整数
    % 出力: 素数の場合true、そうでなければfalse
    
    if n < 2
        result = false;
        return;
    end
    
    if n == 2
        result = true;
        return;
    end
    
    if mod(n, 2) == 0
        result = false;
        return;
    end
    
    % 3から√nまでの奇数で割り切れるかチェック
    sqrt_n = floor(sqrt(n));
    for i = 3:2:sqrt_n
        if mod(n, i) == 0
            result = false;
            return;
        end
    end
    
    result = true;
end

function processNumber(number)
    % 数値を処理する関数
    % 入力: number - 処理する数値
    
    if number <= 0
        fprintf('エラー: 正の整数を入力してください\n');
        return;
    end
    
    if number > 10000000
        fprintf('エラー: 10,000,000以下の数値を入力してください\n');
        return;
    end
    
    if isPrime(number)
        fprintf('%d は素数です\n', number);
    else
        fprintf('%d は素数ではありません\n', number);
    end
end