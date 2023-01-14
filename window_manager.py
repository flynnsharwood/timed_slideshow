import cv2

class WindowManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def create_window(self):
        cv2.namedWindow("Slideshow", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Slideshow", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
    def destroy_window(self):
        cv2.destroyAllWindows()