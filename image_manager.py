import cv2

class ImageManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def load_image(self, image_path):
        img = cv2.imread(image_path)
        aspect_ratio = img.shape[1] / img.shape[0]
        target_width = int(self.screen_height * aspect_ratio)
        if target_width > self.screen_width:
            target_width = self.screen_width
            target_height = int(target_width / aspect_ratio)
        else:
            target_height = self.screen_height
        img = cv2.resize(img, (target_width, target_height))
        height_diff = self.screen_height - target_height
        top_bottom_border = int(height_diff / 2)
        width_diff = self.screen_width - target_width
        left_right_border = int(width_diff / 2)
        img = cv2.copyMakeBorder(img, top_bottom_border, top_bottom_border, left_right_border, left_right_border, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        return img