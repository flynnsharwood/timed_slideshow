import cv2
import random
import time
from . import window_manager
from . import image_manager

class Slideshow:
    def __init__(self, image_paths, duration=3000):
        self.image_paths = image_paths
        self.duration = duration
        self.current_index = 0
        
    def show(self):
        window_manager.create_window()
        random.shuffle(self.image_paths)
        current_index = 0

        for image_path in self.image_paths:
            img = image_manager.read_image(image_path)
            img = image_manager.resize_and_pad(img)
            window_manager.show_image(img, image_path)

            start_time = time.time()
            key = cv2.waitKey(self.duration)
            while (time.time() - start_time) < self.duration/1000:
                remaining_time = int((self.duration/1000 - (time.time() - start_time)))
                remaining_time_str = '{:02d}:{:02d}'.format(int(remaining_time/60), int(remaining_time%60))
                window_manager.show_timer(img, remaining_time_str)
                key = cv2.waitKey(1)
                if key == ord('\r'):
                    window_manager.destroy_window()
                    return current_index
