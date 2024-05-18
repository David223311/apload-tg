import os
import random
import time
from dotenv import load_dotenv
import telegram


def main():
    load_dotenv()
    chat_id = os.environ['CHAT_ID_TG']
    bot = telegram.Bot(token=os.environ['TOKEN_TG'])
    time_between_sending = 14400
    while True:
        folder = 'images'
        files = os.listdir(folder)
        random.shuffle(files)
        for file in files:
            file_path = os.path.join(folder, file)
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id=chat_id, document=f)
            time.sleep(time_between_sending)


if __name__ == '__main__':
    main()
