import os
from urllib.parse import unquote, urlparse
import requests
from download_images import download_image
from dotenv import load_dotenv


def extension_file(url):
    decoder_url = unquote(url)
    parsed_url = urlparse(decoder_url)
    change_path, fullname = os.path.split(parsed_url.path)
    filename, extension = os.path.splitext(fullname)
    return filename, extension


def get_apod_images(nasa_key):
    count = 30
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": nasa_key, "count": count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for apoad_images in response.json():
        if apoad_images.get("media_type") == "image":
            if apoad_images.get("url"):
                apoad_link = apoad_image["hdurl"]
            else:
                apoad_link = apoad_image["url"]
        filename, extension = file_extension(apoad_link)
        path = os.path.join("images", f"{filename}{extension}")
        download_image(apoad_link, path)


def main():
    load_dotenv()
    nasa_key = os.environ['NASA_API']
    get_apod_images(nasa_key)


if __name__ == '__main__':
    main()
