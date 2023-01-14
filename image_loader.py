import os

def load_images(path):
    image_paths = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".jpg") or filepath.endswith(".jpeg") or filepath.endswith(".png"):
                image_paths.append(filepath)
    return image_paths
