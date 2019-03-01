import os

from image_downloader import ImageDownloader as Id


def run():
    downloader = Id()
    for file in os.listdir("imagesToDownload"):
        if file.endswith(".txt"):
            print(os.path.join("/mydir", file))
            downloader.download("testfile.txt")


if __name__ == "__main__":
    run()
