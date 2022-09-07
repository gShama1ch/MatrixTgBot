from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import kb_menu

from loader import dp

@dp.message_handler(text="/menu")
async def menu(message: types.Message):
    await message.answer("Выбери из меню ниже", reply_markup=kb_menu)