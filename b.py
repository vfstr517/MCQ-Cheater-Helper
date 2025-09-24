# This is for .py or .exe runnable environment
import keyboard
import pyautogui
import pytesseract
from PIL import Image
import threading
import tkinter as tk
import io
import requests
import os
import sys

# ==============================
# Config Loaders
# ==============================

def load_api_key(filename="b.txt"):
    try:
        base_path = os.path.dirname(sys.executable)  # works for .exe or .py
        with open(os.path.join(base_path, filename), "r") as f:
            return f.read().strip()
    except Exception as e:
        print(f"❌ Failed to load API key: {e}")
        return None

def load_time(filename="t.txt"):
    try:
        base_path = os.path.dirname(sys.executable)
        with open(os.path.join(base_path, filename), "r") as f:
            return 1000 * int(f.read().strip())
    except Exception as e:
        print(f"❌ Failed to load time, using default 3 seconds: {e}")
        return 3000

def load_region(filename="r.txt"):
    try:
        base_path = os.path.dirname(sys.executable)
        with open(os.path.join(base_path, filename), "r") as f:
            values = f.read().strip().split(",")
            return tuple(map(int, values))
    except Exception as e:
        print(f"❌ Failed to load region, using default (269, 292, 964, 398): {e}")
        return (269, 292, 964, 398)

def load_model(filename="m.txt"):
    try:
        base_path = os.path.dirname(sys.executable)
        with open(os.path.join(base_path, filename), "r") as f:
            return f.read().strip()
    except Exception as e:
        print(f"❌ Failed to load model, using default openai/gpt-4o-mini: {e}")
        return "openai/gpt-4o-mini"

def load_tesseract_path(filename="p.txt"):
    try:
        base_path = os.path.dirname(sys.executable)
        with open(os.path.join(base_path, filename), "r") as f:
            return f.read().strip()
    except Exception as e:
        print(f"❌ Failed to load tesseract path, using default: {e}")
        return r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ==============================
# Initialize Config
# ==============================

stime = load_time()    
OPENROUTER_API_KEY = load_api_key()
OPENROUTER_MODEL = load_model()
tesseract_path = load_tesseract_path()

# Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# ==============================
# Functions
# ==============================

def capture_and_ocr(full_screen=False):
    if full_screen:
        screenshot = pyautogui.screenshot()
    else:
        region = load_region()
        screenshot = pyautogui.screenshot(region=region)

    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    buffer.seek(0)
    img = Image.open(buffer)
    text = pytesseract.image_to_string(img)
    return text.strip()

def get_answer(question):
    try:
        payload = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "system", "content": "Only return the correct answer. No explanation."},
                {"role": "user", "content": question}
            ]
        }
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "https://yourapp.com",
            "X-Title": "mcq-helper",
            "Content-Type": "application/json"
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=20
        )

        if response.status_code == 200:
            data = response.json()
            print("✅ API Raw Response:", data)  # Debugging

            # Try safe parsing
            if "choices" in data and len(data["choices"]) > 0:
                choice = data["choices"][0]

                # Sometimes under "message", sometimes "messages"
                msg = choice.get("message") or choice.get("messages") or {}
                content = msg.get("content", "")

                if content:
                    return content.strip()
                else:
                    return "❌ No content in API response."
            else:
                return "❌ No choices returned from API."
        else:
            print(f"❌ OpenRouter error {response.status_code}: {response.text}")
            return f"❌ API error {response.status_code}"
    except Exception as e:
        print(f"❌ Exception: {e}")
        return f"❌ Exception: {e}"

def show_overlay(answer):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "white")
    root.config(bg="white")

    width, height = 400, 60
    margin = 20
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = screen_width - width - margin + 50
    y = screen_height - height - margin - 50

    root.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(
        root,
        text=answer,
        font=("Arial", 10),
        fg="black",
        bg="white",
        wraplength=width - 20,
        justify="left"
    )
    label.pack(fill="both", expand=True, padx=10, pady=10)

    root.after(stime, root.destroy)
    root.mainloop()

def on_hotkey_trigger(full_screen=False):
    question = capture_and_ocr(full_screen=full_screen)
    print("🖼️ OCR Captured Question:", question)
    if question:
        answer = get_answer(question)
        show_overlay(answer)
    else:
        show_overlay("❌ No text captured")

def start_listener():
    show_overlay("Started")
    keyboard.add_hotkey("F2", lambda: threading.Thread(target=on_hotkey_trigger).start())
    keyboard.add_hotkey("F4", lambda: threading.Thread(target=on_hotkey_trigger, kwargs={"full_screen": True}).start())
    keyboard.wait("esc")
    show_overlay("Stopped")

# ==============================
# Start
# ==============================
start_listener()
