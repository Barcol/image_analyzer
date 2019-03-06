import os

from image_downloader import ImageDownloader as Id
from invalid_images_cleaner import InvalidImagesCleaner as Iic


def run():
    # download_images()  # do not run if database available
    clean_images()


def clean_images():
    cleaner = Iic()
    cleaner.iterate_folders("imagesToBeDeleted")


def download_images():
    """files have to be stored in imagesToDownload directory"""
    downloader = Id()
    downloader.download("beer_in_glasses.txt", "imagesToDownload")
    #for file in os.listdir("imagesToDownload"):
    #    if file.endswith(".txt"):
    #        downloader.download(file, "imagesToDownload")


if __name__ == "__main__":
    run()
