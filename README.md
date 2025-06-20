# 🔐 Image Steganography using LSB

This Python project hides and retrieves secret messages inside PNG images using Least Significant Bit (LSB) steganography.  
Includes both **command-line interface (CLI)** and **Tkinter-based GUI**.

---

## 💻 Features

- Hide secret text messages inside an image  
- Modify LSB of pixel values (spatial domain)  
- 8-bit end marker to stop reading hidden message  
- No visible change to the image  
- GUI for easy interaction and CLI for testing

---

## 📁 Files in This Project

- `encode.py` – CLI script to hide message in image  
- `decode.py` – CLI script to extract message  
- `run_me_stegano_gui.py` – GUI version using Tkinter  
- `input.png` – Sample input image  
- `output.png` – Encoded output image  
- `screenshots/` – Folder with GUI and CLI screenshots

---

## ▶️ How to Run

CLI Version:  
python encode.py  
python decode.py  

GUI Version:  
python run_me_stegano_gui.py

---

## 🖼️ Screenshots

> Add 5 screenshots inside a folder called `screenshots`

- ![Encode CLI](screenshots/encode_cli.png)  
- ![Decode CLI](screenshots/decode_cli.png)  
- ![GUI Message Entry](screenshots/gui_message.png)  
- ![GUI Encode Success](screenshots/gui_success.png)  
- ![GUI Decoded Message](screenshots/gui_decoded.png)

---

## 📚 References

- https://en.wikipedia.org/wiki/Steganography   
- https://pillow.readthedocs.io/   
- https://www.geeksforgeeks.org/image-based-steganography-using-python/ 

---

## 👩‍💻 Author

Parinitha Yadala  
2025 Cybersecurity Mini Project – VNR VJIET
