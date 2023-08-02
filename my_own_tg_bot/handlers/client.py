from aiogram import types, Dispatcher
from imports import dp, bot
from keyboards.client_kb import kb_client
from data_base import sqlite_db


HELP_COMMANDS = """ Добрый день, ниже представлен список основных команд для работы с ботом
/start - начало работы с ботом
/work_time - отображение информации о графике работы магазина
/location - местоположение магазина
"""

# @dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Добро пожаловать, пропишите /help для просмотра основных команд",
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\n https://t.me/stepik_test_project_bot")


# @dp.message_handler(commands=["work_time"])
async def shop_work_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Пн-Пт 9.00 - 18.00, Сб 10.00 - 16.00, Вс - Выходной")


# @dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, HELP_COMMANDS)


# @dp.message_handler(commands=["location"])
async def send_location(message: types.Message):
    await bot.send_location(message.from_user.id, latitude=52.4345, longitude=30.9754)


# @dp.message_handler(commands=["Каталог"])
async def clothes_models(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(shop_work_command, commands=["work_time"])
    dp.register_message_handler(help_command, commands=["help"])
    dp.register_message_handler(send_location, commands=["location"])
    dp.register_message_handler(clothes_models, commands=["Каталог"])