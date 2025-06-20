from PIL import Image

def decode_text(img_path):
    img = Image.open(img_path)
    binary_data = ""
    img_data = list(img.getdata())

    for pixel in img_data:
        for j in range(3):  # RGB
            binary_data += str(pixel[j] & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_text = ""
    for byte in all_bytes:
        if byte == '11111111':
            break
        decoded_text += chr(int(byte, 2))
    return decoded_text


print("🔍 Hidden Message:", decode_text("output.png"))
