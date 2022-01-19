from base64 import encode
from email import message
import json
import datetime

def format_storage():
    localtime = datetime.datetime.today().strftime("%H:%M %d-%m-%Y")
    with open("storage.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    print_message = "Название: " + \
        data["Название"]+"\n"+"Ссылка: "+data["Ссылка"] + \
        "\n"+"Время проверки: "+data["Время"]
    return print_message