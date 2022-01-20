from base64 import encode
from email import message
import json
import datetime

def format_storage():
    localtime = datetime.datetime.today().strftime("%H:%M %d-%m-%Y")
    with open("storage.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    print_message = "Название: " + \
        data["Name"]+"\n"+"Ссылка: "+data["URL"] + \
        "\n"+"Время проверки: "+data["Time"]
    return print_message