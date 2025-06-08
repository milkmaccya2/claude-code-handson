# 🎮 NEON TENNIS 2024 ⚡

A modern, cyberpunk-style tennis game built with Python and Pygame featuring stunning neon visuals, particle effects, and futuristic aesthetics.

![Game Preview](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🌟 Visual Effects
- **Cyberpunk Neon Aesthetic** - Stunning cyan, pink, green, and orange color scheme
- **Real-time Particle Effects** - Trail particles, explosion effects, and ambient particles
- **Glow Effects** - Dynamic glowing elements throughout the game
- **Futuristic Grid Background** - Animated grid with floating particles
- **Animated UI Elements** - Pulsing scores, combo counters, and transitions

### ⚡ Gameplay Features
- **Combo System** - Ball changes color after 5+ consecutive hits
- **Intelligent AI** - Predictive AI that anticipates ball trajectory
- **Progressive Speed** - Ball speed increases with each paddle hit
- **Score Particle Explosions** - Visual feedback when scoring
- **First to 7 Wins** - Extended gameplay for more excitement

### 🎯 Special Effects
- **Paddle Motion Trails** - Visual trails when paddles move
- **Ball Collision Explosions** - Particle bursts on wall/paddle hits
- **Pulsating Score Display** - Dynamic score visualization
- **Intro Screen** - Stylized welcome screen with instructions

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation & Running

1. **Clone or download the game files**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the game:**
   ```bash
   python tennis_game.py
   ```

### Alternative: Use Pre-built Executable

For users without Python installed:

**macOS:**
- Run `./dist/NeonTennis2024` from terminal
- Or double-click `NeonTennis2024.app` in Finder

## 🎮 Controls

| Key | Action |
|-----|--------|
| `W` or `↑` | Move paddle up |
| `S` or `↓` | Move paddle down |
| `SPACE` | Restart game (when game over) |
| `ESC` | Quit game |
| `Any Key` | Start game (from intro screen) |

## 🛠️ Technical Details

### Dependencies
- **pygame 2.5.2** - Game engine and graphics
- **random** - Random number generation
- **math** - Mathematical calculations for effects
- **sys** - System operations

### Architecture
- **Object-Oriented Design** - Clean class structure for game components
- **Particle System** - Efficient particle management for visual effects
- **Real-time Rendering** - 60 FPS smooth gameplay
- **Collision Detection** - Precise rectangle-based collision system

### Performance
- **Optimized Particle System** - Automatic cleanup of expired particles
- **Efficient Rendering** - Alpha blending for smooth glow effects
- **Memory Management** - Proper resource cleanup and management

## 📁 Project Structure

```
python_app/
├── tennis_game.py          # Main game file
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── dist/                  # Executable files
│   ├── NeonTennis2024     # Standalone executable
│   └── NeonTennis2024.app/ # macOS app bundle
└── build/                 # Build artifacts (auto-generated)
```

## 🎨 Game Elements

### Visual Components
- **Player Paddle** - Cyan colored with particle trails
- **AI Paddle** - Pink colored with smart movement
- **Ball** - Dynamic color changing with trail effects
- **Background** - Animated grid with floating particles
- **UI** - Glowing text with pulsing animations

### Particle Effects
- **Trail Particles** - Follow moving objects
- **Hit Particles** - Explosion effects on collisions
- **Score Particles** - Celebration effects when scoring
- **Background Particles** - Ambient floating elements

## 🔧 Building Executable

To create your own executable:

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Build executable:**
   ```bash
   pyinstaller --onefile --windowed --name "NeonTennis2024" tennis_game.py
   ```

3. **Find executable in `dist/` folder**

## 🎯 Game Rules

1. **Objective:** First player to reach 7 points wins
2. **Scoring:** Ball reaching opponent's side scores a point
3. **Speed:** Ball speed increases with each paddle hit
4. **Combo:** After 5+ consecutive hits, ball changes color
5. **AI Difficulty:** AI uses predictive movement for challenge

## 🚀 Future Enhancements

- 🔊 Sound effects and background music
- 🎵 Dynamic soundtrack that changes with gameplay
- 💥 Power-ups and special abilities
- 🏆 Tournament mode with multiple rounds
- 👥 Two-player local multiplayer
- 📊 Statistics tracking and high scores
- 🎨 Multiple visual themes

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available under the MIT License.

---

**Enjoy playing NEON TENNIS 2024! ⚡🎮**

*Created with passion for retro-futuristic gaming aesthetics*