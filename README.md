```markdown
# 🎓 Quizzy - A Python Quiz App

**Quizzy** is a simple, GUI-based quiz game built with Python. It fetches True/False questions from the Open Trivia Database API and presents them in an interactive interface. The app features a modern design using `ttkbootstrap`.

---

## 🚀 Features

- ✅ Real-time question display  
- 🎯 Instant feedback with color transitions  
- 🎨 Modern UI with `ttkbootstrap` styling  
- 📊 Live score updates  
- 🌐 Auto-fetch questions from OpenTDB API  

---

## 🖥️ Tech Stack

- Python 3.10+
- `tkinter` + `ttkbootstrap` for GUI
- `requests` for API communication

---

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rogue-Sensei-Dev/Quizzy-App.git
   cd quizzy
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   - On any platform:
     ```bash
     python main.py
     ```

   - Or simply **double-click `run.bat`** (Windows only)

---

## 📁 Project Structure

```
quizzy/
├── main.py
├── data.py
├── question_model.py
├── quiz_brain.py
├── ui.py
├── images/
│   ├── true.png
│   └── false.png
├── requirements.txt
└── run.bat
```

---

## 📡 API Source

Questions are fetched from:  
👉 [Open Trivia Database](https://opentdb.com/)

---

## 📜 License

This project is licensed under the MIT License.

---
