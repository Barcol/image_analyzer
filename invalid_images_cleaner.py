import os
from glob import glob
import cv2
import numpy as np


class InvalidImagesCleaner:
    def __init__(self):
        self.patterns_to_delete = {}
        self.images_to_be_verifed = {}

    def iterate_folders(self, mold_directory, *folders_with_images):
        for pattern_file_path in glob(f"{mold_directory}/*.jpg"):
            self.patterns_to_delete[pattern_file_path] = cv2.imread(pattern_file_path)
        for folder in folders_with_images:
            for file_path in glob(f"{folder}/*.jpg"):
                self.images_to_be_verifed[file_path] = cv2.imread(file_path)
        self.delete_none_types()
        self.delete_useless_images()

    def delete_none_types(self):
        for image in self.patterns_to_delete:
            if self.patterns_to_delete[image] is None:
                os.remove(image)
                del self.patterns_to_delete[image]
        for image in self.images_to_be_verifed:
            if self.patterns_to_delete[image] is None:
                os.remove(image)
                del self.images_to_be_verifed[image]

    def delete_useless_images(self):
        for pattern_image in self.patterns_to_delete:
            for image in self.images_to_be_verifed:
                if self.patterns_to_delete[pattern_image].shape == self.images_to_be_verifed[image].shape and not\
                        (np.bitwise_xor(self.patterns_to_delete[pattern_image], self.images_to_be_verifed[image]).any()):
                    os.remove(image)
                    del self.images_to_be_verifed[image]
