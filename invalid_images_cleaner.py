import os

import cv2
import numpy as np


class InvalidImagesCleaner:
    def __init__(self):
        pass

    def iterate_folders(self, mold_directory):
        for file in os.listdir(mold_directory):
            if file.endswith(".jpg"):
                delete_mold = cv2.imread(mold_directory + "/" + file, 0)  # opens a file as an example for bad images
                self.delete_useless_images("beer_in_bottles", delete_mold)  # check first folder
                self.delete_useless_images("beer_in_glasses", delete_mold)  # check second folder

    @staticmethod
    def delete_useless_images(path: str, image_mold):
        for file in os.listdir(path):
            image = cv2.imread(path + "/" + file, 0)  # read a file in folder (for example in beers_in_glass) as matrix
            try:
                if image.shape == image_mold.shape and not(np.bitwise_xor(image, image_mold).any()):
                    os.remove(path + "/" + file)
            except AttributeError:
                print(type(image), type(image_mold), path, file)
