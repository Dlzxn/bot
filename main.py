from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter, CommandObject
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from dotenv import load_dotenv
import os
import sqlite3
import telebot
from aiogram.types import FSInputFile
from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram import types
import base64
import logging.config
import logging
import asyncio

#пакеты
from log_cfg.def_log import start_log, user_new
from log_cfg.logging_conf import logging_config
from admin import adm_rout
from defs.defd import ref_prov, db_table_val, from_bd, zamena_para
from users import users_rout






async def main():
    logging.config.dictConfig(logging_config) #загрузка настроек
    start_log()
    user_new('Dlzxn', 321423432)
    load_dotenv()
    # Создаем объекты бота и диспетчера
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    #роутеры
    dp.include_router(adm_rout.router)
    dp.include_router(users_rout.router)
    # Запускаем поллинг
    await dp.start_polling(bot)




asyncio.run(main())