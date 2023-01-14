import cv2
import os
import pyautogui
import random
import time

screen_width, screen_height = pyautogui.size()

path = r"C:\Users\harsh\Desktop\sfw"
image_paths = []

for subdir, dirs, files in os.walk(path):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".jpg") or filepath.endswith(".jpeg") or filepath.endswith(".png"):
            image_paths.append(filepath)

random.shuffle(image_paths)

duration = 30000 #  30 seconds
cv2.namedWindow("Slideshow", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

cv2.namedWindow("Slideshow", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Slideshow", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

random.shuffle(image_paths)

current_index = 0

for image_path in image_paths:
    img = cv2.imread(image_path)
    aspect_ratio = img.shape[1] / img.shape[0]
    target_width = int(screen_height * aspect_ratio)
    if target_width > screen_width:
        target_width = screen_width
        target_height = int(target_width / aspect_ratio)
    else:
        target_height = screen_height
    img = cv2.resize(img, (target_width, target_height))
    height_diff = screen_height - target_height
    top_bottom_border = int(height_diff / 2)
    width_diff = screen_width - target_width
    left_right_border = int(width_diff / 2)
    img = cv2.copyMakeBorder(img, top_bottom_border, top_bottom_border, left_right_border, left_right_border, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    cv2.imshow("Slideshow", img)
    start_time = time.time()
    key = cv2.waitKey(duration)
    while (time.time() - start_time) < duration/1000:
        remaining_time = int((duration/1000 - (time.time() - start_time)))
        remaining_time_str = '{:02d}:{:02d}'.format(int(remaining_time/60), int(remaining_time%60))
        cv2.putText(img, remaining_time_str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
        cv2.rectangle(img, (0, 0), (550, 150), (0, 0, 0), -1)
        cv2.imshow("Slideshow", img)
        key = cv2.waitKey(1)
        if key == ord('\r'):
            break
        elif key == ord('n'):
            current_index = (current_index + 1) % len(image_paths)
            break
        elif key == ord('p'):
            current_index = (current_index - 1) % len(image_paths)
            break
# show the next image
img = cv2.imread(image_paths[current_index])
aspect_ratio = img.shape[1] / img.shape[0]
target_width = int(screen_height * aspect_ratio)
if target_width > screen_width:
    target_width = screen_width
    target_height = int(target_width / aspect_ratio)
else:
    target_height = screen_height
    img = cv2.resize(img, (target_width, target_height))
    height_diff = screen_height - target_height
    top_bottom_border = int(height_diff / 2)
    width_diff = screen_width - target_width
    left_right_border = int(width_diff / 2)
    img = cv2.copyMakeBorder(img, top_bottom_border, top_bottom_border, left_right_border, left_right_border, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    cv2.imshow("Slideshow", img)
    start_time = time.time()
    cv2.putText(img, remaining_time_str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
    cv2.rectangle(img, (0, 0), (550, 150), (0, 0, 0), -1)
    key = cv2.waitKey(duration)


cv2.destroyAllWindows()
