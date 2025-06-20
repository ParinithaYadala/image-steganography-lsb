# Image Steganography using LSB (Python Project)

This project hides and retrieves secret text messages within PNG images using Least Significant Bit (LSB) steganography.

## 💻 Features

- Encode and decode messages using **Python**
- CLI version using `encode.py` and `decode.py`
- GUI version using **Tkinter**
- Messages are hidden without altering the image visually
- 8-bit end marker used to detect end of message

## 📁 Files Included

- `encode.py` – Command-line encoder
- `decode.py` – Command-line decoder
- `run_me_stegano_gui.py` – GUI version using Tkinter
- `input.png` – Sample input image
- `output.png` – Output image (optional)
- `screenshots/` – GUI & terminal outputs

## 🖼️ Screenshots

![Encoding CLI](screenshots/encode.png)  
![Decoding CLI](screenshots/decode.png)  
![GUI Success](screenshots/gui_success.png)  
![GUI Decoded Message](screenshots/gui_output.png)  
![File Selection](screenshots/gui_file_picker.png)

## 🚀 How to Run

### ▶ CLI Version
python encode.py
python decode.py
