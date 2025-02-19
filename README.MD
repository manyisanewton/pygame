# 🐍 Snake Game with Pygame

A fun Snake Game built using **Python** and **Pygame** with sound effects and music background play.

## 🎮 Features
- Classic snake gameplay 🐍
- Sound effects for eating and game over 🔊
- Background music 🎵
- Dynamic snake speed adjustment 🚀
- Pause & Resume functionality ⏸️▶️

## 📷 Game Preview
(Screenshot or GIF of gameplay here)

---

## 🚀 Installation
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/snake-game.git
cd snake-game
```

### 2️⃣ **Set Up Virtual Environment** (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate    # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Game**
```bash
python snake_game.py
```

---

## 🛠️ Building an Executable (For Friends & Family)

### **Convert to EXE (Standalone Application)**
```bash
pyinstaller --onefile --windowed snake_game.py
```
- This will generate an executable in `dist/` folder.

### **Run the Executable**
```bash
./dist/snake_game  # On Linux
start dist\snake_game.exe  # On Windows
```

---

## 🌍 Deploying with GitHub Releases
### 1️⃣ **Initialize Git & Push Code**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/snake-game.git
git push -u origin main
```

### 2️⃣ **Create a New Release on GitHub**
1. Go to **GitHub Repository** → Click **Releases** → **New Release**
2. Upload the EXE file (`dist/snake_game.exe`)
3. Give it a version (e.g., `v1.0`), add a description, and publish.

---

## 📝 Troubleshooting
### If `git push` hangs:
```bash
git push --verbose
git gc --aggressive --prune=now
git repack -a -d --depth=250 --window=250
git push origin main
```

### If EXE is not working:
```bash
pyinstaller --onefile --noconsole snake_game.py
```

---

## 💡 Future Improvements
✅ Add a leaderboard 📊  
✅ More themes & skins 🎨  
✅ Multiplayer mode 🕹️

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author
**Newton Manyisa**  
GitHub: [@manyisanewton](https://github.com/manyisanewton)  

---

🎮 Enjoy the game! 🚀
