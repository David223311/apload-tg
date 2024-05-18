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

Для получения необходимых изображений необходимо написать:
```
python main.py
```
## Переменные окружения
Часть настроек проекта берётся из переменных окружения. Переменные окружения - это переменные, значения которых
присваиваются программе Python извне. Чтобы их определить, создайте файл `.env `рядом с `main.py` и запишите туда данные в таком
формате: ПЕРЕМЕННАЯ=значение.

Пример содержания файла `.env`:
```
NASA_API_KEY = "nasa-token"
TG_TOKEN = "bot-token"
TG_CHAT_ID = "@chat_id"
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
