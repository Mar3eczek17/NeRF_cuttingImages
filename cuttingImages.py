import os
import random
from PIL import Image, ImageDraw

def insert_black_squares(image, square_size):
    width, height = image.size

    draw = ImageDraw.Draw(image)

    # Calculate the new square size
    new_square_size = square_size

    # Generate random coordinates for the top-left corner of the square
    left = random.randint(0, width - new_square_size)
    top = random.randint(0, height - new_square_size)

    # Insert a black square at the chosen position
    draw.rectangle((left, top, left + new_square_size, top + new_square_size), fill="black")

    return image

def process_images_in_folder(folder_path, square_size, percentage):
    files = os.listdir(folder_path)
    num_images = int(len(files) * percentage)

    selected_files = random.sample(files, num_images)

    for file in selected_files:
        if file.endswith('.png'):
            image_path = os.path.join(folder_path, file)
            image = Image.open(image_path)
            modified_image = insert_black_squares(image, square_size)
            modified_image.save(image_path)

# Example usage:
folder_path = 'lego'
square_size = 80
percentage = 0.1  # 10% randomly selected images

process_images_in_folder(folder_path, square_size, percentage)
