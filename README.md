# 🔐 Image Steganography using LSB

This Python project hides and retrieves secret messages inside PNG images using Least Significant Bit (LSB) steganography.  
It includes both a **Command-Line Interface (CLI)** and a user-friendly **Tkinter-based GUI** for encoding and decoding hidden messages.

---

## 💻 Features

- Embed secret text into images using LSB method  
- 8-bit end marker to indicate end of message  
- Original image remains visually unchanged  
- CLI for fast testing, GUI for easy usage  
- Uses Python Pillow for pixel-level manipulation

---

## 📁 Project Structure

- `encode.py` – CLI tool to hide messages  
- `decode.py` – CLI tool to extract messages  
- `run_me_stegano_gui.py` – GUI application using Tkinter  
- `input.png` – Sample input image  
- `output.png` – Output image after encoding  
- `screenshots/` – Proof images from CLI and GUI runs

---

## ▶️ How to Run

### 🔹 CLI Version  
python encode.py  
python decode.py

### 🔹 GUI Version  
python run_me_stegano_gui.py

---

## 🖼️ Screenshots

> The following screenshots demonstrate working of both CLI and GUI:

- ![Encode CLI](screenshots/Encode%20CLI.png)  
- ![Decode CLI](screenshots/Decode%20CLI.png)  
- ![GUI Success Popup](screenshots/GUI%20success%20popup.png)  
- ![GUI Input & Output](screenshots/GUI%20input%20%26%20output.png)  
- ![File Chooser Dialog](screenshots/File%20chooser%20dialog%20for%20decoding.png)

---

## 📚 References

- https://en.wikipedia.org/wiki/Steganography  
- https://pillow.readthedocs.io/  
- https://www.geeksforgeeks.org/image-based-steganography-using-python/

---

## 👩‍💻 Author

Parinitha Yadala  
**EDUNET FOUNDATION - IBM SKILLSBUILD - CYBER SECURITY - 6 WEEKS INTERNSHIP MAY 2025**
