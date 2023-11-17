from PIL import Image, ImageDraw

def get_bar_width(character):
    if 'a' <= character <= 'z':
        return ord(character) - ord('a') + 1
    elif 'A' <= character <= 'Z':
        return ord(character) - ord('A') + 1
    else:
        return 0  # Empty space

def encode(input_string):
    # Step 1: Create an empty canvas of size 400 X 800.
    canvas_width = 800
    canvas_height = 400
    image = Image.new("1", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(image)

    # Step 2: Define variables and step.
    step = 9
    bar_start_row = 10
    bar_end_row = 350
    empty_space_start_row = 150
    empty_space_end_row = 250
    bar_start_column = step

    # Step 3: loop through the entered string character by character and encode (draw) the barcode
    for character in input_string:
        bar_width = get_bar_width(character)
        if bar_width == 0:
            draw.rectangle([bar_start_column, empty_space_start_row, bar_start_column + bar_width, empty_space_end_row], fill="black")
        else:
            draw.rectangle([bar_start_column, bar_start_row - 1, bar_start_column + bar_width, bar_end_row], fill="black")
        bar_start_column += bar_width + step + 1

    # Step 4: Write the result as in image
    image.save("Output.png")

encode("Abbas Cheddad")