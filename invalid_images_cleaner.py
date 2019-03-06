import os
from glob import glob
import cv2
import numpy as np


class InvalidImagesCleaner:
    def iterate_folders(self, mold_directory, *folders_with_images):
        patterns_to_delete = {}
        images_to_be_verifed = {}
        for pattern_file_path in glob(f"{mold_directory}/*.jpg"):
            patterns_to_delete[pattern_file_path] = cv2.imread(pattern_file_path)
        for folder in folders_with_images:
            for file_path in glob(f"{folder}/*.jpg"):
                images_to_be_verifed[file_path] = cv2.imread(file_path)
        self.delete_none_types(patterns_to_delete, images_to_be_verifed)
        self.delete_useless_images(patterns_to_delete, images_to_be_verifed)

    @staticmethod
    def delete_none_types(patterns_to_delete, images_to_be_verifed):
        for image in patterns_to_delete.copy():
            if patterns_to_delete[image] is None:
                os.remove(image)
                del patterns_to_delete[image]
        for image in images_to_be_verifed.copy():
            if images_to_be_verifed[image] is None:
                os.remove(image)
                del images_to_be_verifed[image]

    @staticmethod
    def delete_useless_images(patterns_to_delete, images_to_be_verifed):
        for pattern_image in patterns_to_delete:
            for image in images_to_be_verifed.copy():
                if (patterns_to_delete[pattern_image].shape == images_to_be_verifed[image].shape
                        and not np.bitwise_xor(patterns_to_delete[pattern_image], images_to_be_verifed[image]).any()):
                    os.remove(image)
