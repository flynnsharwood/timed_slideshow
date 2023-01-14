import cv2

def resize_image(img, screen_width, screen_height):
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
    return img
