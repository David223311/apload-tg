import requests
from download_images import download_image


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    spacex_links = response.json()['links']['flickr']['original']
    for spacex_number, link in enumerate(spacex_links):
        filename = f'images/spacex{spacex_number}.jpg'
        download_image(link, filename)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
