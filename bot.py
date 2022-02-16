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

#init bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#commands block
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Sup, i'm bot. Write /help to see what i can do.")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Write /packages to see the list of packages for arch instalation")

@dp.message_handler(commands=['packages'])
async def process_show_source_command(message: types.Message):
    await message.reply(output_reply("package_reply"))

@dp.message_handler(commands=['addingUser'])
async def process_show_source_command(message: types.Message):
    await message.reply(output_reply("add_user_reply"))

#to check out is bot working
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    #start
    executor.start_polling(dp)
