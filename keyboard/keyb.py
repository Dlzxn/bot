from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)

from keyboard.buttons.button import url_button_my_otn, url_button_1, url_button_return, url_button_del_otn, url_button_del


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