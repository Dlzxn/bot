from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F

router = Router()

@router.message(Command(commands="adm"))
async def adm_list(message: Message):
    await message.answer(f'Вы-админ')