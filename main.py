from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from dotenv import load_dotenv
import os
import sqlite3
import telebot
from defs.def_1 import start_comand

load_dotenv()

# Создаем объекты бота и диспетчера
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart)
async def start_comande(message: Message):
    start_comand(message)




# Запускаем поллинг
dp.run_polling(bot)
