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
from aiogram.types import FSInputFile
from defs.defd import ref_prov, db_table_val

load_dotenv()

# Создаем объекты бота и диспетчера
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


#инлайн кнопки
url_button_1=InlineKeyboardButton(
     text="Оформить покупку",
     callback_data='button_buy_press'
)
#обьект инлайн клавиатуры
keyboard_menu=InlineKeyboardMarkup(
     inline_keyboard=[[url_button_1]]
)

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Вас приветствует бот по продаже вирт!\n'
                         f'Для взаимодействия отправьте /start\n'
                         )


@dp.message(CommandStart)
async def start_cm(message: Message):
    if ref_prov(message.from_user.id)==False:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    await message.answer_photo(photo=FSInputFile('image/menu.jpg', filename='кру'),
                        caption=f'Приветствую тебя в боте любви!\n'
                        f'Для построения отношений введите /newpara',
                        reply_markup=keyboard_menu
                        )
    print("dddd")



# Запускаем поллинг
dp.run_polling(bot)
