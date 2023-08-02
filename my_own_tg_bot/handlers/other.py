from aiogram import types, Dispatcher
from my_own_tg_bot.imports import dp
import json, string


# @dp.message_handler()
async def mat_filter(message: types.Message):
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(" ")}\
        .intersection(set(json.load(open("not_mat.json")))):
        await message.reply("Маты запрещены")
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mat_filter)