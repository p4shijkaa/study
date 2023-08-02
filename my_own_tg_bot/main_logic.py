from aiogram import executor
from imports import dp
from handlers import admin, client, other
from data_base import sqlite_db


async def on_startup(_):
    print("Our bot is start working")
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)