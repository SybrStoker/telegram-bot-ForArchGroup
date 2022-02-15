from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

#i will change it soon for now it's like test.
#Use file in next update
text = """
Пакеты первой необходимости:

Пример:
Номер."Название пакета" - (описание);

/*При перечислении пакетов, нужно что-то выбрать или использовать все вместе при желании, допустим чтобы попробовать все и решить, что нравиться больше.*/


1."base" - ();

2. "linux" - ();

3.linux-firmware - (прошивка);

4.base-devel - ();

5.networkmanager - (программа для автоматического подключения интернета);

6.grub - (загрузчик системы);

7.thunar - (проводник или же файловый менеджер. Графическая версия для перехода по каталогам);

8.xorg - (Демон для запуска графической оболочки);

9."plasma", "gnome", "lxqt" - (Графическая Оболочка);

10.sddm - (графический менеджер, позволяет выбирать ГО и пользователя);

11. "nvidia" - (nvidia драйвер для большей части видюх);

12. "vim" - (консольный текстовый редактор);

13. "net-tools" - (набор команд для работы с интернетом, сюда же входит ipconfig);

14. "wget" - (консольная ультилита для загрузки файлов через URL);

15. "git" - (консольная ультилита для поддержки версий программ);

16. "firefox" - (браузер);

17."alacritty" - (терминал);

18. "htop" - (терминальная ультилита которая позволяеет увидеть загруженность железа и запущенные процессы с демонами);
"""

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
    await message.reply(text)

#to check out is bot working
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    #start
    executor.start_polling(dp)
