# オンラインホワイトボード

リアルタイムで複数人が同時に描画できるオンラインホワイトボードアプリです。

## 🌐 デプロイ済みアプリ

**🎨 ライブデモ**: https://online-whiteboard-men5rxzyt-hiroaki-yokoyamas-projects.vercel.app

**🖥️ サーバー**: https://online-whiteboard-1749345891-2ded1504fb2f.herokuapp.com

## ✨ 機能

### 🎨 描画ツール
- **✏️ ペンツール**: 自由な線描画
- **🗑️ 消しゴムツール**: 部分的な消去
- **📏 線の太さ調整**: 1-50pxまで調整可能
- **🎨 色選択**: カラーピッカーで自由な色選択
- **🗑️ 全消去**: ワンクリックでキャンバス全体をクリア
- **💾 ダウンロード**: PNG形式で作品を保存

### 🔄 リアルタイム機能
- **多人数同時描画**: 複数ユーザーが同時に描画可能
- **即座の同期**: 描画がリアルタイムで他のユーザーに反映
- **描画履歴の保持**: 新規接続時に既存の描画を自動表示
- **接続状況表示**: 現在の接続ユーザー数をリアルタイム表示

### 📱 デバイス対応
- **マウス操作**: デスクトップでの直感的な描画
- **タッチ操作**: タブレット・スマートフォン対応
- **レスポンシブデザイン**: 様々な画面サイズに対応

## 🛠️ 技術スタック

### フロントエンド
- **HTML5 Canvas**: 高性能な描画エンジン
- **Vanilla JavaScript**: 軽量でシンプルな実装
- **Socket.IO Client**: リアルタイム通信

### バックエンド
- **Node.js**: サーバーサイドランタイム
- **Express.js**: Webアプリケーションフレームワーク
- **Socket.IO**: WebSocketベースのリアルタイム通信
- **CORS**: クロスオリジンリソース共有対応

### インフラ・デプロイ
- **Vercel**: クライアント側の高速CDN配信
- **Heroku**: サーバー側のクラウドホスティング
- **Git**: バージョン管理とデプロイ自動化

## 🚀 ローカル開発

### 必要な環境
- Node.js (v16.0.0以上)
- npm (v8.0.0以上)
- Git

### クライアント側の起動
```bash
# 依存関係のインストール
npm install

# 開発サーバー起動
npm run dev

# http://localhost:3000 でアクセス
```

### サーバー側の起動
```bash
# サーバー用設定ファイルをコピー
cp server-package.json package.json

# 依存関係のインストール
npm install

# 開発サーバー起動
npm run dev

# サーバーがポート3000で起動
```

## 📦 デプロイ手順

### Vercel（クライアント）への初回デプロイ
```bash
# Vercel CLIのインストール
npm i -g vercel

# デプロイ実行
vercel

# 本番環境にデプロイ
vercel --prod
```

### Heroku（サーバー）への初回デプロイ
```bash
# Heroku CLIでログイン
heroku login

# Gitリポジトリ初期化
git init
git add .
git commit -m "Initial commit"

# Herokuアプリ作成
heroku create your-app-name

# サーバー設定をメインに設定
cp server-package.json package.json

# デプロイ実行
git push heroku main
```

### 本番環境での設定更新

1. **クライアント側**: `index.html`のサーバーURL更新
2. **サーバー側**: `server.js`のCORS設定にクライアントURL追加

## 🔧 カスタマイズ

### 描画設定の変更
```javascript
// index.html内のWhiteBoardクラス
this.currentSize = 3;        // デフォルトの線の太さ
this.currentColor = '#000000'; // デフォルトの色
```

### キャンバスサイズの変更
```html
<!-- index.html -->
<canvas id="whiteboard" width="1200" height="800"></canvas>
```

### 描画履歴の保存件数
```javascript
// server.js
if (drawingHistory.length > 10000) {
    drawingHistory = drawingHistory.slice(-8000);
}
```

## 🐛 トラブルシューティング

### 接続できない場合
1. ブラウザの開発者ツール（F12）でコンソールエラーを確認
2. サーバーのログを確認: `heroku logs --tail -a your-app-name`
3. CORS設定が正しいか確認

### 描画が同期されない場合
1. Socket.IO接続状況をコンソールで確認
2. ネットワーク接続を確認
3. ブラウザのキャッシュをクリア

### パフォーマンスが低下する場合
1. 描画履歴が大きすぎる可能性（全消去を実行）
2. 複数タブで同時に開いている場合は1つにする
3. ブラウザの拡張機能を無効化してテスト

## 📄 ライセンス

MIT License

## 🤝 コントリビューション

プルリクエストやイシューの報告を歓迎します。

## 📞 サポート

バグ報告や機能要求は、GitHubのIssuesページでお知らせください。