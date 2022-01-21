# установка базового образа (host OS)
FROM python:3.8
#RUN apt-get update && apt-get -y install cron
# установка рабочей директории в контейнере
WORKDIR /usr/src/app
# копирование файла зависимостей в рабочую директорию
COPY requirements .
# установка зависимостей
RUN pip install --no-cache-dir -r requirements
# копирование содержимого локальной директории src в рабочую директорию
COPY . .
# отдельное копирование крон задания
#COPY app_cron /etc/cron.d/app_cron

# сменить время на московское
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
#RUN chmod 0644 /etc/cron.d/app_cron
#RUN crontab /etc/cron.d/app_cron
# команда, выполняемая при запуске контейнера
CMD [ "python", "./telebot.py" ]