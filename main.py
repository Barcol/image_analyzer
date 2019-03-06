import os

from image_downloader import ImageDownloader as Id
from invalid_images_cleaner import InvalidImagesCleaner as Iic


def run():
    # download_images()  # run if database not available
    # clean_images()  # run if "this image is not available" images are present
    pass


def clean_images():
    cleaner = Iic()
    cleaner.iterate_folders("imagesToBeDeleted", "beer_in_glasses", "beer_in_bottles")


def download_images():
    """files have to be stored in imagesToDownload directory"""
    downloader = Id()
    downloader.download("beer_in_glasses.txt", "imagesToDownload")
    #for file in os.listdir("imagesToDownload"):
    #    if file.endswith(".txt"):
    #        downloader.download(file, "imagesToDownload")


if __name__ == "__main__":
    run()
