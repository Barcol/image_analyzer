import os
from glob import glob

import cv2
import numpy as np
from keras.models import load_model
from scipy import misc

from image_downloader import ImageDownloader as Id
from invalid_images_cleaner import InvalidImagesCleaner as Iic
from model_generator import ModelGenerator


def run():
    # download_images()  # run if database not available
    # clean_images()  # run if "this image is not available" images are present
    generate_model()  # run if no model available
    model = load_model('model.h5')
    for image_path in glob("szklarian_beers/*"):
        image = cv2.imread(image_path)
        image = misc.imresize(image, (100, 100, 3))
        image = np.array(image)
        image = image / image.max()
        result = model.predict(np.array([image]))
        print(image_path, f" to na {int(round(100 * result[0][0]))}% butelka," +
              f"a na {int(round(100 * result[0][1]))}% szklanka ")

def generate_model():
    generator = ModelGenerator()
    generator.prepare_model("beer_in_bottles", "beer_in_glasses")


def clean_images():
    cleaner = Iic()
    cleaner.iterate_folders("imagesToBeDeleted", "beer_in_glasses", "beer_in_bottles")


def download_images():
    """txt files have to be stored in imagesToDownload directory"""
    downloader = Id()
    for file in os.listdir("imagesToDownload"):
        if file.endswith(".txt"):
            downloader.download(file, "imagesToDownload")


if __name__ == "__main__":
    run()
