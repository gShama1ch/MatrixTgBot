from aiogram import types
from loader import dp
from keyboards.inline import to_prod_markup

@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await message.answer(f'Я MatrixBot v1.0', reply_markup=to_prod_markup)
