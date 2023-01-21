import cv2
import random
import time
from window_manager import WindowManager
from image_manager import ImageManager

class Slideshow:
    def __init__(self, image_paths, duration=3000):
        self.image_paths = image_paths
        self.duration = duration
        self.current_index = 0
        self.image_manager = ImageManager()
        self.window_manager = WindowManager()

    def show(self):
        self.window_manager.create_window()
        if len(self.image_paths) == 0:
            print("No images found in the directory")
            self.window_manager.destroy_window()
            return
        random.shuffle(self.image_paths)

        for image_path in self.image_paths:
            img = self.image_manager.read_image(image_path)
            img = self.image_manager.resize_and_pad(img)
            self.window_manager.show_image(img, image_path)

            start_time = time.time()
            while (time.time() - start_time) < self.duration/1000:
                if cv2.getWindowProperty(self.window_manager.window_name, cv2.WND_PROP_VISIBLE) < 1:
                    self.window_manager.destroy_window()
                    return
                remaining_time = int((self.duration/1000 - (time.time() - start_time)))
                remaining_time_str = '{:02d}:{:02d}'.format(int(remaining_time/60), int(remaining_time%60))
                self.window_manager.show_timer(img, remaining_time_str)
                key = cv2.waitKey(1)
                if key == ord('\r'):
                    self.window_manager.destroy_window()
                    return 
