from asyncio.log import logger
import json
import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("token")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


def format_storage():
    with open("okey_minimum_price.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    print_message = "Название: " + data["title"]+"\n"+"Цена за килограмм: "+str(data["price_kg"])+" "+data["currency"] + \
        "\n"+"Вес: "+str(data["weight"])+" "+data["measure"]+"\n"+"Ссылка: " + \
        data["link"] + "\n"+"Время проверки: 16:14 21-01-2022"
    logger.info("formatted message is \n"+print_message)
    return print_message


@dp.message_handler()
async def cmd_test1(message: types.Message):
    await message.reply(format_storage())
    logger.info("successful reading format_storage()")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
