from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# this is main menu block
btnInstallation = KeyboardButton("Установка")
btnOther = KeyboardButton("Другое")
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInstallation,\
                                                            btnOther)
btnBackToMain = KeyboardButton("Главное меню")

# this is menu of button other
btnAddU = KeyboardButton("Добавление users")
btnGrub = KeyboardButton("Запуск ОС GRUB2")
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnAddU,\
                                                            btnGrub,\
                                                            btnBackToMain)
#this is btnInstallation menu
btnPackages = KeyboardButton("Пакеты для pacstrap")
installationMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPackages,\
                                                                btnBackToMain)
