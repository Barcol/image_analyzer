"""This image downloader only works on text files that contains exactly one .jpg link in every line"""
import os
import urllib.request

from tqdm import tqdm


class ImageDownloader:
    def __init__(self):
        pass

    def __download(self, images):
        newpath = f"./{self.__file_to_folder_name(images)}"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        with open(images, "r") as file:
            for number, line in enumerate(tqdm(file)):
                urllib.request.urlretrieve(line, f".{images}/{number}.jpg")

    @staticmethod
    def __file_to_folder_name(name):
        for position, sign in enumerate(name):
            if sign == ".":
                return name[0:position]
        return name
