import os
import requests
import datetime
from download_images import download_image
from dotenv import load_dotenv


def get_epic_images(nasa_key):
    count = 5
    url = "https://api.nasa.gov/EPIC/api/natural/image"
    params = {"api_key":nasa_key , "count": count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for epic_images in response.json():
        data = epic_images["date"]
        name = epic_images["image"]
        photo_date = datetime.datetime.fromisoformat(data)
        photo_date = photo_date.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{name}.png"
        path = os.path.join("images", f"{name}.png")
        download_image(url, path, params)


def main():
    load_dotenv()
    nasa_key = os.environ['NASA_TOKEN']
    get_epic_images(nasa_key)
    

if __name__ == '__main__':
    main()
