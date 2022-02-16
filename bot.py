import menu

import pathlib
from pathlib import Path

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

def output_reply(file_name:str):
    """Find the needed replies

    We take the name of reply and seek it in rep, when we found it,
    give the inner text as output"""
    with open(Path("replies", file_name)) as file:
        text = file.read()
    return text
def main() -> None:
    #init bot
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    #commands block
    @dp.message_handler(commands=['start'])
    async def process_start_command(message: types.Message):
        await bot.send_message(message.from_user.id,"Чем могу помочь?",\
                                reply_markup = menu.mainMenu)

    @dp.message_handler(commands=['help'])
    async def process_help_command(message: types.Message):
        await message.reply("Напиши /start, чтобы запустить главное меню")

    #to check out is bot working
    @dp.message_handler()
    async def navigation(message: types.Message):
        match message.text:
            case "Установка":
                await bot.send_message(message.from_user.id,message.text,\
                        reply_markup = menu.installationMenu)
            case "Главное меню":
                await bot.send_message(message.from_user.id,message.text,\
                        reply_markup = menu.mainMenu)
            case "Пакеты для pacstrap":
                await message.reply(output_reply("package_reply"))
            case "Другое":
                await bot.send_message(message.from_user.id,message.text,\
                        reply_markup = menu.otherMenu)
            case "Добавление users":
                await message.reply(output_reply("add_user_reply"))
            case "Запуск ОС GRUB2":
                await message.reply(output_reply("grub2_init_reply"))
            case "спс":
                await message.reply("Незачто")

    executor.start_polling(dp)

if __name__ == '__main__':
    main()
