from PIL import Image, ImageDraw, ImageFont
import random

def generate_bingo_card():
    bingo_card = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    bingo_card['B'] = random.sample(range(1, 16), 5)
    bingo_card['I'] = random.sample(range(16, 31), 5)
    bingo_card['N'] = random.sample(range(31, 46), 5)
    bingo_card['G'] = random.sample(range(46, 61), 5)
    bingo_card['O'] = random.sample(range(61, 76), 5)
    bingo_card['N'][2] = "FREE"
    return bingo_card

def create_bingo_image(bingo_card, filename="Bingo_Card.png"):
    # Image dimensions
    img_width, img_height = 600, 700
    cell_size = 100
    x_offset = (img_width - cell_size * 5) // 2  # Center horizontally
    y_offset = 150  # Top margin for grid

    # Create blank image with white background
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    # Fonts (adjust paths if necessary)
    try:
        font_title = ImageFont.truetype("arial.ttf", 40)
        font_cells = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        # Fallback to default fonts if specific font files are not found
        font_title = ImageFont.load_default()
        font_cells = ImageFont.load_default()

    # Draw title
    title_text = "B I N G O"
    title_bbox = draw.textbbox((0, 0), title_text, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    title_x = (img_width - title_width) // 2
    draw.text((title_x, 50), title_text, fill="black", font=font_title)

    # Draw grid
    for i in range(6):  # 5 rows + 1 for borders
        # Horizontal lines
        y = y_offset + i * cell_size
        draw.line([(x_offset, y), (x_offset + 5 * cell_size, y)], fill="black", width=2)

        # Vertical lines
        x = x_offset + i * cell_size
        draw.line([(x, y_offset), (x, y_offset + 5 * cell_size)], fill="black", width=2)

    # Fill cells
    for row in range(5):
        for col, letter in enumerate("BINGO"):
            value = bingo_card[letter][row]
            text = str(value)
            if value == "FREE":
                text = "FREE"
            text_bbox = draw.textbbox((0, 0), text, font=font_cells)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            cell_x = x_offset + col * cell_size + (cell_size - text_width) // 2
            cell_y = y_offset + row * cell_size + (cell_size - text_height) // 2
            draw.text((cell_x, cell_y), text, fill="black", font=font_cells)

    # Save image
    img.save(filename)
    print(f"Bingo card saved as {filename}!")

# Generate and save Bingo card as an image
bingo_card = generate_bingo_card()
create_bingo_image(bingo_card)
