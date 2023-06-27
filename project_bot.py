"""FINITE STATE MACHINE"""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboard import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlite import db_start, create_profile, edit_profile


storage = MemoryStorage()

API_TOKEN = '6003655761:AAF8d5hdEw_OTeMiPg9t3bLCPOqXVUARzQ0'

bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()


def get_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("/create"))
    return kb


def get_cancel_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("/cancel"))
    return kb


@dp.message_handler(commands=["cancel"], state="*")
async def get_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return


    await state.finish()
    await message.reply("Вы прервали создание анкеты", reply_markup=get_kb())

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Welcome to profile - /create",
                         reply_markup=get_kb())

@dp.message_handler(commands=["create"])
async def cmd_create(message: types.Message):
    await message.reply("Create your profile", reply_markup=get_cancel_kb())
    await ProfileStatesGroup.photo.set()

@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply("Это не фото")


@dp.message_handler(content_types=["photo"], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id

    await message.reply("теперь отправь свое имя")
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.text

    await message.reply("Сколько тебе лет?")
    await ProfileStatesGroup.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ProfileStatesGroup.age)
async def check_photo(message: types.Message):
    await message.reply("возраст должен быть цифрой")


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text

    await message.reply("А теперь расскажи немного о себе")
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text

    await message.reply("Ваша анкета успешно создана")
    await state.finish()



async def on_startup(_):
    print("Бот запущен!")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
