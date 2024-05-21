# Космический Телеграм
Проект создан для выкладивания фотографи связанных с космосом. Программа автоматически создает отдельные директории для каждого набора изображений.

## Как установить
Скачайте необходимые файлы, затем используйте `pip` (или `pip3` , если есть конфликт с Python 2) для установки зависимостей и
установить зависимости. Зависимости можно установить командой, представленной ниже. Создайте бота в [BotFather](https://t.me/BotFather). Создайте новый
Telegram канал.

Установите зависимости командой:
```
pip install -r requirements.txt
```
Для запуска скрипта у вас уже должен быть установлен Python 3.

Для получения изображения Nasa_epic необходимо написать:
```
python get_epic_image.py
```
Для получения изображения Nasa_apoad необходимо написать:
```
python get_apod_image.py
```
Для получения изображения SpaceX необходимо написать:
```
python fetch_spacex_last_launch.py
```
Для отправки необходимых изображений необходимо написать:
```
python tg_apload.py
```
## Переменные окружения
Часть настроек проекта берётся из переменных окружения. Переменные окружения - это переменные, значения которых
присваиваются программе Python извне. Чтобы их определить, создайте файл `.env `рядом с `main.py` и запишите туда данные в таком
формате: ПЕРЕМЕННАЯ=значение.z

Пример содержания файла `.env`:
```
NASA_API = "nasa-token"
TG_TOKEN = "bot-token"
TG_CHAT_ID = "@chat_id"
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
