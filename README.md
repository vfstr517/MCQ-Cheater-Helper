# MCQ-Cheater-Helper
# 📘 MCQ Helper – OCR + AI Answer Overlay

MCQ Helper is a lightweight Python/EXE tool that:  
- Captures a question from your screen using **OCR (Tesseract)**  
- Sends it to **OpenRouter AI** to get the correct answer  
- Displays the answer in a **transparent overlay** on your screen  
- Works with hotkeys:  
  - `F2` → Capture **region** (from `r.txt`)  
  - `F4` → Capture **full screen**  
  - `Esc` → Exit  

---

## 🚀 Features
- Works as both **Python script (`.py`)** and **standalone EXE (`.exe`)**  
- Reads config from text files (easy to change without editing code)  
- Transparent Tkinter overlay for answers  
- Supports multiple models (default: `openai/gpt-4o-mini`)  
- Customizable capture region, display time, and Tesseract path  

---

## **Important**
- The a.py is for python running environment
- The b.py is .exe environment (apparently the code structure for exe changes in Python)
- The Region Finder.py is used for reducing tokens(basically to save money) by taking the nessary part screen shot only
- **If you want to avoid confusion just use f4 but this might discloused sensitive information to the AI model**
- **The exe is in dist folder**

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/vfstr517/MCQ-Cheater-Helper
cd MCQ-Cheater-Helper
```

### 2. Install dependencies (Python users only)
pip install -r requirements.txt
Dependencies:

- keyboard
- pyautogui
- pytesseract
- Pillow
- requests
- tkinter (comes with Python on Windows)

### 3. Install Tesseract OCR

Download from [UB Mannheim Tesseract Build](https://github.com/UB-Mannheim/tesseract/wiki).  
Default installation path:
```bash
C:\Program Files\Tesseract-OCR\tesseract.exe
```
or you can customise this using p.txt.

## 📂 Config Files

Place these files in the same folder as your .py or .exe:
| File  | Purpose                   | Example                                      |
| ----- | ------------------------- | -------------------------------------------- |
| b.txt | OpenRouter API key        | sk-or-v1-xxxxxxxx                            |
| t.txt | Overlay time (seconds)    | 3                                            |
| r.txt | OCR region (x,y,w,h)      | 269,292,964,398                              |
| m.txt | Model name (optional)     | openai/gpt-4o-mini                           |
| p.txt | Tesseract path (optional) | C:\Program Files\Tesseract-OCR\tesseract.exe |

## ▶️ Running
### Python
```bash
python mcq_helper.py
```
### EXE
**After building (go to below path), double-click:**
```bash
dist/mcq_helper.exe
```

**Hotkeys:**
- F2 → Capture region OCR + AI answer
- F4 → Capture full screen OCR + AI answer
- Esc → Exit

## 📦 Build EXE (Optional):
If you want to do changes to the code just use this on b.py to convert to **.exe**
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole b.py
```
Your exe will be in dist/mcq_helper.exe.

## 📝 Notes

- Requires a valid [OpenRouter API key](https://openrouter.ai/) in b.txt
- Internet connection required
- Works on Windows (tested), may need tweaks for Linux/Mac

## 📜 License

MIT License – free to use and modify.
```bash
---
### 📄 `requirements.txt`
```txt
keyboard
pyautogui
pytesseract
Pillow
requests
```
