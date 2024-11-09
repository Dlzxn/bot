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
from defs.defd import ref_prov, db_table_val, from_bd, zamena_para
from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram import types
import base64
import logging.config
import logging

#конфиг логов
import yaml #для logging_settings на yaml


with open('log_cfg/logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)


load_dotenv()
# Создаем объекты бота и диспетчера
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


#инлайн кнопки
url_button_my_otn=InlineKeyboardButton(
     text="Мои отношения",
     callback_data='button_my_otn'
)
url_button_1=InlineKeyboardButton(
     text="Создать отношения",
     callback_data='button_new_otn')
url_button_return=InlineKeyboardButton(
     text="Вернуться",
     callback_data='button_return'
)
url_button_del_otn=InlineKeyboardButton(
     text="Удалить отношения",
     callback_data='button_del_otn'
)
url_button_del=InlineKeyboardButton(
     text="ДА", #согласие на удаление отношений
     callback_data='button_del'
)
#обьект инлайн клавиатуры
keyboard_menu=InlineKeyboardMarkup(
     inline_keyboard=[[url_button_1]]
)
keyboard_menu_true=InlineKeyboardMarkup(
     inline_keyboard=[[url_button_my_otn]]
)
keyboard_menu_return=InlineKeyboardMarkup(
     inline_keyboard=[[url_button_return]]
)
keyboard_menu_otn=InlineKeyboardMarkup(
     inline_keyboard=[[url_button_return], [url_button_del_otn]]
)



@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Вас приветствует бот бот для парочек!\n'
                         f'Здесь вы можете настраивать и развивать свои отношения\n'
                         f'Для взаимодействия отправьте /start\n'
                         )

@dp.message(CommandStart)
async def start_cm(message: types.Message):
    if ref_prov(message.from_user.id)==False:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    if from_bd(4, message.from_user.id)==None:
        await message.answer_photo(photo=FSInputFile('image/menu.jpg', filename='кру'),
                        caption=f'Приветствую тебя в боте любви!\n'
                        f'Для построения отношений выберите "Создать отношения"',
                        reply_markup=keyboard_menu
                        )
    else:
        await message.answer_photo(photo=FSInputFile('image/menu.jpg', filename='кру'),
                            caption=f'Приветствую тебя в боте любви!\n'
                            f'Уже бежишь к своей половинке?',
                            reply_markup=keyboard_menu_true)
    print((int(decode_payload(message.text[7:])))!=message.from_user.id)
    if (message.text[7:])!="" and (int(decode_payload(message.text[7:])))!=message.from_user.id:
        zamena_para(int(decode_payload(message.text[7:])), message.from_user.id)
        await message.answer(f'Теперь ВЫ и {from_bd(1, int(decode_payload(message.text[7:])))} пара!')

@dp.callback_query(F.data=="button_return")
async def start_cm(callback: CallbackQuery):
    if from_bd(4, callback.message.chat.id)==None:
        await callback.message.answer_photo(photo=FSInputFile('image/menu.jpg', filename='кру'),
                        caption=f'Приветствую тебя в боте любви!\n'
                        f'Для построения отношений выберите "Создать отношения"',
                        reply_markup=keyboard_menu
                        )
    else:
        await callback.message.answer_photo(photo=FSInputFile('image/menu.jpg', filename='кру'),
                            caption=f'Приветствую тебя в боте любви!\n'
                            f'Уже бежишь к своей половинке?',
                            reply_markup=keyboard_menu_true)



#кнопка соззать отношения
@dp.callback_query(F.data=='button_new_otn')
async def mt_referal_menu (callback: CallbackQuery, state: FSMContext, bot: Bot):
    link = await create_start_link(bot,str(callback.from_user.id), encode=True)
    print("f")
    print(link)
    await callback.message.edit_caption(caption=f'Для того, что бы добавить пару\n'
                         f'Ваша половинка должна перейти по следующей ссылке:\n'
                         f'{link}',
                         media=FSInputFile('image/love.jpg'),
                         reply_markup=keyboard_menu_return
                        )
    await callback.answer()

#смена кнопки по проходу меню-отношения-----------------edit
@dp.callback_query(F.data=='button_my_otn')
async def process_button_buy_press(callback: CallbackQuery):
    if callback.message.text != "Ваши отношения":
        if from_bd(4, callback.from_user.id):
            await callback.message.edit_caption(
                caption=f'Ваши отношения:\n'
                f'Ваша пара {from_bd(1, callback.from_user.id)}\n'
                f'Уровень отношений: {from_bd(6, callback.from_user.id)}\n'
                f'Прогресс: {from_bd(5, callback.from_user.id)}\n'
                f'Любовь творит чудеса!',
                reply_markup=keyboard_menu_otn
        )
    await callback.answer()


# Запускаем поллинг
dp.run_polling(bot)