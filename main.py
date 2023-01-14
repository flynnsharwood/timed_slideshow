import os
import random
import time
import cv2
import pyautogui
import logging

from directory_selector import select_directory
from image_loader import load_images
from slideshow import start_slideshow

# Select directory containing images
path = select_directory()

# Load images from directory
image_paths = load_images(path)

# Shuffle images
random.shuffle(image_paths)

# Start slideshow
start_slideshow(image_paths)
