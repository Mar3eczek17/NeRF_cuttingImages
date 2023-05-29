import os
import random
import cv2
import numpy as np
from PIL import Image

def add_gaussian_noise(image, square_size):
    width, height = image.size

    # Convert PIL Image to OpenCV format
    image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Generate Gaussian noise with the same size as the square
    mean = 0
    std_dev = 30
    noise = np.random.normal(mean, std_dev, (square_size, square_size, 3)).astype(np.uint8)

    # Randomly select the position of the square
    left = random.randint(0, width - square_size)
    top = random.randint(0, height - square_size)

    # Add the noise to the corresponding region of the image
    noisy_image = image_np.copy()
    noisy_image[top:top+square_size, left:left+square_size, :] += noise

    # Convert the noisy image back to PIL format
    noisy_image_pil = Image.fromarray(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))

    return noisy_image_pil

def process_images_in_folder(folder_path, square_size, percentage):
    files = os.listdir(folder_path)
    num_images = int(len(files) * percentage)

    selected_files = random.sample(files, num_images)

    for file in selected_files:
        if file.endswith('.png'):
            image_path = os.path.join(folder_path, file)
            image = Image.open(image_path)
            noisy_image = add_gaussian_noise(image, square_size)
            noisy_image.save(image_path)

# Example usage:
folder_path = 'lego'
square_size = 80
percentage = 0.1  # 10% randomly selected images

process_images_in_folder(folder_path, square_size, percentage)