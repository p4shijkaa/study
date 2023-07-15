# ЕЩЕ РАЗ ПРОСМОТРЕТЬ И ИЗУЧИТЬ

# import requests
# import time
#
#
# API_URL: str = 'https://api.telegram.org/bot'
# API_CATS_URL: str = 'https://aws.random.cat/meow'
# BOT_TOKEN: str = '6003655761:AAF8d5hdEw_OTeMiPg9t3bLCPOqXVUARzQ0'
# ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
#
# offset: int = -2
# counter: int = 0
# cat_response: requests.Response
# cat_link: str
#
#
# while counter < 100:
#     print('attempt =', counter)
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_response = requests.get(API_CATS_URL)
#             if cat_response.status_code == 200:
#                 cat_link = cat_response.json()['file']
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
#             else:
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
#
#     time.sleep(1)
#     counter += 1



# polling


# API_URL: str = 'https://api.telegram.org/bot'
# BOT_TOKEN: str = '6003655761:AAF8d5hdEw_OTeMiPg9t3bLCPOqXVUARzQ0'
# offset: int = -2
# updates: dict
#
#
# def do_something() -> None:
#     print('Был апдейт')
#
#
# while True:
#     start_time = time.time()
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             do_something()
#
#     time.sleep(3)
#     end_time = time.time()
#     print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')


# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import Command
# from aiogram.types import Message, ContentType
#
#
# API_TOKEN = '6003655761:AAF8d5hdEw_OTeMiPg9t3bLCPOqXVUARzQ0'
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(Command(commands=["start"]))
# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
#
#
# @dp.message(Command(commands=['help']))
# async def process_help_command(message: Message):
#     await message.answer('Напиши мне что-нибудь и в ответ '
#                          'я пришлю тебе твое сообщение')
#
# @dp.message(Command(commands=['Sasha']))
# async def say_Sasha_hello(message: Message):
#     await message.answer("Привет Саша")
#
#
# @dp.message(F.photo)
# async def send_photo_echo(message: Message):
#     await message.reply_photo(message.photo[0].file_id)
#
#
# @dp.message(F.sticker)
# async def send_sticker_echo(message: Message):
#     await message.reply_sticker(message.sticker.file_id)
#
#
# @dp.message(F.video)
# async def send_video_echo(message: Message):
#     await message.reply_video(message.video.file_id)
#
#
# @dp.message()
# async def process_any_update(message: Message):
#     print(message)
#     await message.answer(text='Вы что-то прислали')
#
#
# if __name__ == '__main__':
#     dp.run_polling(bot)


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6003655761:AAF8d5hdEw_OTeMiPg9t3bLCPOqXVUARzQ0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text="random link",
                           url="https://www.youtube.com/watch?v=XXVs_8wXl_A")
ikb.add(ib1)


COMMAND_HELPS = """
/help - список команд,
/start - запуск бота,
/description - описание бота,
/photo - отправка фотографии
"""

@dp.message_handler(commands=["links"])
async def get_links(message: types.Message):
    await message.answer(text="inline keyboard",
                         reply_markup=ikb)

# @dp.message_handler(commands=["help"])
# async def get_help(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text=COMMAND_HELPS)
#
# @dp.message_handler(commands=["start"])
# async def get_start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text="добро пожаловать",
#                            reply_markup=kb)
#
# @dp.message_handler(commands=["description"])
# async def get_description(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text="наш бот умеет отправлять фотографии",
#                            reply_markup=ReplyKeyboardMarkup())
#
#
# @dp.message_handler(commands=["photo"])
# async def get_photo(message: types.Message):
#     await bot.send_photo(chat_id=message.from_user.id,
#                          photo="https://www.google.com/imgres?imgurl=http%3A%2F%2Fzviazda.by%2Fsites%2Fdefault%2Ffiles%2Ffield%2Fimage%2F30-6_kopiya_3.jpg&tbnid=5II5A7qnDadrgM&vet=12ahUKEwiErubu4qb_AhWLwSoKHZn5BWAQMygFegUIARDtAQ..i&imgrefurl=https%3A%2F%2Fzviazda.by%2Fru%2Fnews%2F20190529%2F1559146658-vozdushnye-shariki-vredyat-prirode-i-ee-dikim-obitatelyam&docid=8UK2xgOnYQkkKM&w=784&h=593&q=%D1%88%D0%B0%D1%80%D0%B8%D0%BA%D0%B8&ved=2ahUKEwiErubu4qb_AhWLwSoKHZn5BWAQMygFegUIARDtAQ")
#
# @dp.message_handler(commands=["location"])
# async def get_loc(message: types.Message):
#     await bot.send_location(chat_id=message.from_user.id,
#                            longitude=30.9754,
#                            latitude=52.4345)

# @dp.message_handler(commands=["give"])
# async def get_sticker(message: types.Message):
#     await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEI-9lkYhV7lEffeFyHcqNfjf9yUTVNqwAC8gADVp29ChCdi3ZTetJkLwQ")
#
#
# @dp.message_handler(commands=["emoji"])
# async def get_emoji(message: types.Message):
#     await message.reply(message.text + "😉")

async def on_startup(_):
    print("Бот был запущен")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

