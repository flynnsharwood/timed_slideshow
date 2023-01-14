import logging

def log_image_path(image_path):
    logging.basicConfig(filename='image_paths.log', level=logging.INFO)
    logging.info(image_path)
