from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)

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