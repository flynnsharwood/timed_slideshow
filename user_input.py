import cv2

def handle_user_input(img, duration):
    start_time = time.time()
    key = cv2.waitKey(duration)
    while (time.time() - start_time) < duration/1000:
        remaining_time = int((duration/1000 - (time.time() - start_time)))
        remaining_time_str = '{:02d}:{:02d}'.format(int(remaining_time/60), int(remaining_time%60))
        cv2.putText(img, remaining_time_str, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
        cv2.rectangle(img, (0, 0), (550, 150), (0, 0, 0), -1)
        cv2.imshow("Slideshow", img)
        key = cv2.waitKey(1)
        if key == ord('\r'):
            cv2.destroyAllWindows()
            return
        elif key == ord('n'):
            current_index = (current_index + 1) % len(image_paths)
            break
        elif key == ord('p'):
            current_index = (current_index - 1) % len(image_paths)
            break
