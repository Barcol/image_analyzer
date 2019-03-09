import os

from image_downloader import ImageDownloader as Id
from invalid_images_cleaner import InvalidImagesCleaner as Iic
from model_generator import ModelGenerator


def run():
    # download_images()  # run if database not available
    # clean_images()  # run if "this image is not available" images are present
    generate_model()


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
