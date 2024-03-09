import os
import requests


def download_image(url, path, params=None):
    os.makedirs("images", exist_ok=True)
    response = requests.get(url, params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
