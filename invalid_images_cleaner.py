import cv2
import os


class InvalidImagesCleaner:
    def __init__(self):
        pass

    def iterate_folders(self, mold_directory):
        for file in os.listdir(mold_directory):
            if file.endswith(".jpg"):
                delete_mold = cv2.imread(file, 0)
                self.delete_useless_images("beer_in_bottles", delete_mold)
                self.delete_useless_images("beer_in_glasses", delete_mold)

    @staticmethod
    def delete_useless_images(path, image_mold):
        for file in os.listdir(path):
            image = cv2.imread(file, 0)
            if image == image_mold:
                os.remove(file)
