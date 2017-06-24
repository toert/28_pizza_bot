# Телеграм Бот Для Пицерии

В рамках данного проекта был реализован телеграм бот с привязкой к реляционной БД, изменение данных в которой производится с помощью Flask-Admin

# How to Use

## Подготовка к запуску

Шаг 1. Зарегистрируйте нового бота в Телеграм, написав [@BotFather](https://telegram.me/botfather) .

Шаг 2. Полученный токен(как `BOT_TOKEN`), а также URI базы данных(как `DB_URI`), секретный ключ приложения(как `SECRET_KEY`), а также желаемый логин(`login`) и пароль(`password`) админ-панели добавьте в ваше Окружение среды. [Как это сделать в Windows?](http://ru.stackoverflow.com/questions/153628/%D0%9A%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%83%D1%8E-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-path-%D0%BF%D1%83%D1%82%D1%8C) [Linux?](http://ru.stackoverflow.com/questions/228/%D0%9A%D0%B0%D0%BA-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%83%D1%8E-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2-linux-unix)

Шаг 3. Запускаем `create_db.py`, чтобы создать базу данных

Шаг 4. Загружаем в неё данные из листа скриптом `fill_db.py`

Шаг 5. Запускаем бота скриптом `bot.py`

## Использование

 Для изменения данных запускаем `server.py` и открываем в браузере [http://127.0.0.1:5000/admin](http://127.0.0.1:5000/admin)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
