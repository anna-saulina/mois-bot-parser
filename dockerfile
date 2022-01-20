# установка базового образа (host OS)
FROM python:3.8
# установка рабочей директории в контейнере
WORKDIR /usr/src/app
# копирование файла зависимостей в рабочую директорию
COPY requirements .
# установка зависимостей
RUN pip install --no-cache-dir -r requirements
# копирование содержимого локальной директории src в рабочую директорию
COPY . .
# сменить время на московское
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# команда, выполняемая при запуске контейнера
CMD [ "python", "./telebot.py" ]