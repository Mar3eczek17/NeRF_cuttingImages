import os
import random
from PIL import Image, ImageDraw

def insert_black_squares(image, square_size):
    width, height = image.size

    draw = ImageDraw.Draw(image)

    # Oblicz nowy rozmiar kwadratu
    new_square_size = square_size

    # Wylosuj losowe współrzędne lewego górnego rogu kwadratu
    left = random.randint(0, width - new_square_size)
    top = random.randint(0, height - new_square_size)

    # Wstaw czarne pole w wybranym miejscu
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
            modified_image.save(f"legoMod/modified_{file}")

# Przykład użycia:
folder_path = 'lego'
square_size = 80
percentage = 0.1  # 10% losowo wybranych obrazów

process_images_in_folder(folder_path, square_size, percentage)