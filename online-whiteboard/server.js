const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
const server = http.createServer(app);

app.use(cors({
    origin: [
        "http://localhost:3000",
        "http://localhost:5000", 
        "https://online-whiteboard-2k0bc0un5-hiroaki-yokoyamas-projects.vercel.app",
        "https://online-whiteboard-gwo7hphwb-hiroaki-yokoyamas-projects.vercel.app"
    ],
    credentials: true
}));

const io = socketIo(server, {
    cors: {
        origin: [
            "http://localhost:3000",
            "http://localhost:5000",
            "https://online-whiteboard-2k0bc0un5-hiroaki-yokoyamas-projects.vercel.app",
            "https://online-whiteboard-gwo7hphwb-hiroaki-yokoyamas-projects.vercel.app"
        ],
        methods: ["GET", "POST"],
        credentials: true
    }
});

app.use(express.json());
app.use(express.static('public'));

let connectedUsers = 0;
let drawingHistory = [];

app.get('/', (req, res) => {
    res.json({ 
        message: 'オンラインホワイトボードサーバー',
        status: 'running',
        connectedUsers: connectedUsers
    });
});

app.get('/health', (req, res) => {
    res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

io.on('connection', (socket) => {
    console.log('ユーザーが接続しました:', socket.id);
    connectedUsers++;
    
    console.log('現在の接続ユーザー数:', connectedUsers);
    io.emit('user-count', connectedUsers);
    
    // 接続時に既存の描画履歴を送信
    console.log('描画履歴チェック:', drawingHistory.length, '件');
    if (drawingHistory.length > 0) {
        console.log('描画履歴を送信:', drawingHistory.length, '件');
        // 少し遅延を入れて確実に送信
        setTimeout(() => {
            socket.emit('drawing-history', drawingHistory);
            console.log('描画履歴送信完了');
        }, 100);
    } else {
        console.log('描画履歴なし - 空のキャンバスで開始');
    }

    socket.on('drawing', (data) => {
        console.log('描画データを受信:', {
            tool: data.tool,
            color: data.color,
            size: data.size,
            x0: data.x0,
            y0: data.y0,
            x1: data.x1,
            y1: data.y1
        });
        
        const drawingData = {
            ...data,
            timestamp: Date.now(),
            socketId: socket.id
        };
        
        drawingHistory.push(drawingData);
        
        if (drawingHistory.length > 10000) {
            drawingHistory = drawingHistory.slice(-8000);
            console.log('描画履歴をトリム:', drawingHistory.length, '件');
        }
        
        // 他のクライアントにブロードキャスト
        socket.broadcast.emit('drawing', data);
        console.log('描画データをブロードキャスト完了');
    });

    socket.on('clear-canvas', () => {
        console.log('キャンバスクリア要求を受信');
        drawingHistory = [];
        socket.broadcast.emit('clear-canvas');
        console.log('キャンバスクリアをブロードキャスト完了');
    });

    socket.on('disconnect', (reason) => {
        console.log('ユーザーが切断しました:', socket.id, 'reason:', reason);
        connectedUsers = Math.max(0, connectedUsers - 1);
        console.log('現在の接続ユーザー数:', connectedUsers);
        io.emit('user-count', connectedUsers);
    });

    socket.on('error', (error) => {
        console.error('Socket error:', error);
    });

    socket.on('connect_error', (error) => {
        console.error('Socket connect error:', error);
    });
});

server.on('error', (error) => {
    console.error('Server error:', error);
});

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
    console.log(`サーバーがポート ${PORT} で起動しました`);
    console.log(`環境: ${process.env.NODE_ENV || 'development'}`);
});

process.on('SIGTERM', () => {
    console.log('SIGTERM received, shutting down gracefully');
    server.close(() => {
        console.log('Process terminated');
    });
});

process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error);
    process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
    process.exit(1);
});