"""This image downloader only works on text files that contains exactly one .jpg link in every line"""
import os
import urllib.request
import urllib.error

from tqdm import tqdm


class ImageDownloader:
    def __init__(self):
        pass

    def download(self, images: str, path: str):
        newpath = f"./{self.__file_to_directory_name(images)}"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        with open(path + "/" + images, "r") as file:
            for number, link in (tqdm(list(enumerate(file)))):
                try:
                    urllib.request.urlretrieve(link, f"{self.__file_to_directory_name(images)}/{number}.jpg")
                except urllib.error.HTTPError:
                    print(f"\n{link} does not contain any image!")
                except urllib.error.URLError:
                    print(f"\n{link} is not a valid image link!")
                except ValueError:
                    print("Invalid link")
                except TimeoutError:
                    print("Connection time out")
                except ConnectionResetError:
                    print("Connection was suddenly closed")
                except Exception:
                    print("For fuck's sake, what now")

    @staticmethod
    def __file_to_directory_name(name):
        for position, sign in enumerate(name):
            if sign == ".":
                return name[0:position]
        return name
