from aiogram import types
from keyboards.default import kb_menu
from loader import dp


@dp.message_handler()
async def command_hello(message: types.Message):
    await message.answer(f'Пожалуйста исользуй что-нибудь из клавиатуры)', reply_markup=kb_menu)