from PIL import Image

def encode_text(img_path, message, output_path):
    img = Image.open(img_path)
    binary_msg = ''.join(format(ord(c), '08b') for c in message) + '1111111111111110'  
    data_index = 0
    img_data = list(img.getdata())

    for i in range(len(img_data)):
        pixel = list(img_data[i])
        for j in range(3):  
            if data_index < len(binary_msg):
                pixel[j] = pixel[j] & ~1 | int(binary_msg[data_index])
                data_index += 1
        img_data[i] = tuple(pixel)
        if data_index >= len(binary_msg):
            break

    img.putdata(img_data)
    img.save(output_path)
    print("✅ Message hidden successfully in", output_path)


encode_text("input.png", "Hi EDUNET, this is Parinitha and this is your secret message!", "output.png")
