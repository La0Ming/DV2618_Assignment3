from PIL import Image

def decode(image_path):
    # Step 1: Read the image
    image = Image.open(image_path)

    image_width, image_height = image.size
    middle_row = 200
    barcode_string = ""
    w = 0

    # Step 2: Scan the image horizontally through the middle line (row 200)
    for column in range(image_width):
        pixel = image.getpixel((column, middle_row))

        if pixel == 0:
            w += 1
        else:
            if w == 1:
                barcode_string += " "
            else:
                character = w - 1
                
                if 1 <= character <= 26:
                    barcode_string += chr(ord("A") + character - 1)
            
            w = 0

    return barcode_string

decoded_string = decode("Output.png")