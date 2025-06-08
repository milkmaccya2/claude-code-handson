# 🐱 猫タイマーアプリ

可愛い猫の画像を使った、カワイイデザインのタイマーアプリです。

## 📁 ファイル構成

- `timer.html` - メインのタイマーアプリ（HTML/CSS/JavaScript）
- `timer_cat.png` - AI生成した可愛い猫の画像
- `cat_image_generator.py` - 猫画像生成用Pythonスクリプト
- `image_generator.py` - 動物画像生成用Pythonスクリプト（サンプル）

## 🚀 使い方

### タイマーアプリの起動

1. `timer.html` をブラウザで開く
2. 分・秒を設定
3. 「スタート」ボタンでタイマー開始

### 機能

- ⏰ 分・秒でタイマー設定
- ▶️ スタート・一時停止・リセット機能
- 🎉 時間終了時のアニメーション
- 🔊 終了時の音とアラート通知
- 🎨 ピンクベースの可愛いデザイン

## 🖼️ 画像生成

### 必要なライブラリ

```bash
pip install openai requests
```

### APIキーの設定

```bash
# 環境変数で設定
export OPENAI_API_KEY="your-openai-api-key"

# または、Pythonファイル内で直接設定
api_key = "your-openai-api-key"
```

### 画像生成の実行

```bash
# 猫画像生成
python cat_image_generator.py

# その他の動物画像生成（サンプル）
python image_generator.py
```

## 🎨 デザイン特徴

- カワイイ系アニメスタイルの猫画像
- ピンクとホワイトの優しい色合い
- ふんわりとしたグラデーション背景
- 丸みを帯びたボタンデザイン
- レスポンシブ対応

## 📝 注意事項

- OpenAI APIキーが必要です
- 画像生成にはインターネット接続が必要
- APIの利用料金が発生する場合があります

---

🐱 可愛い猫ちゃんと一緒に時間管理を楽しんでください！