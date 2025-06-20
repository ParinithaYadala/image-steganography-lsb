import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def encode_image():
    file_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    if not file_path:
        return
    message = message_entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Enter a secret message.")
        return

    binary_msg = ''.join(format(ord(c), '08b') for c in message) + '11111111'
    img = Image.open(file_path)
    data_index = 0
    img_data = list(img.getdata())

    for i in range(len(img_data)):
        pixel = list(img_data[i])
        for j in range(3):  # RGB
            if data_index < len(binary_msg):
                pixel[j] = pixel[j] & ~1 | int(binary_msg[data_index])
                data_index += 1
        img_data[i] = tuple(pixel)
        if data_index >= len(binary_msg):
            break

    img.putdata(img_data)
    output_path = os.path.splitext(file_path)[0] + "_encoded.png"
    img.save(output_path)
    messagebox.showinfo("Success", f"Message hidden!\nSaved as:\n{output_path}")

def decode_image():
    file_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    if not file_path:
        return
    img = Image.open(file_path)
    binary_data = ""
    img_data = list(img.getdata())

    for pixel in img_data:
        for j in range(3):
            binary_data += str(pixel[j] & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_text = ""
    for byte in all_bytes:
        if byte == '11111111':
            break
        decoded_text += chr(int(byte, 2))

    decoded_output.delete("1.0", tk.END)
    decoded_output.insert(tk.END, decoded_text)

# Create GUI Window
root = tk.Tk()
root.title("LSB Image Steganography")
root.geometry("500x400")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Image Steganography using LSB", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
title.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

message_label = tk.Label(frame, text="Enter Secret Message:", fg="white", bg="#1e1e1e")
message_label.grid(row=0, column=0, sticky="w")
message_entry = tk.Text(frame, width=50, height=4)
message_entry.grid(row=1, column=0, padx=5, pady=5)

encode_btn = tk.Button(root, text="Encode Message into Image", command=encode_image, bg="#4caf50", fg="white", padx=10)
encode_btn.pack(pady=10)

decode_btn = tk.Button(root, text="Decode Message from Image", command=decode_image, bg="#2196f3", fg="white", padx=10)
decode_btn.pack(pady=10)

decoded_label = tk.Label(root, text="Decoded Message:", fg="white", bg="#1e1e1e")
decoded_label.pack()
decoded_output = tk.Text(root, width=50, height=5)
decoded_output.pack(pady=5)

root.mainloop()
