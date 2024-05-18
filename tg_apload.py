import os
import random
import time
from dotenv import load_dotenv
import telegram


def main():
    load_dotenv()

    bot = telegram.Bot(token=os.environ['TOKEN_TG'])

    while True:
        folder = 'images'
        files = os.listdir(folder)
        random.shuffle(files)
        for file in files:
            file_path = os.path.join(folder, file)
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id=os.environ['CHAT_ID_TG'], document=f)
            time.sleep(14400)


if __name__ == '__main__':
    main()
