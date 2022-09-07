from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.types import CallbackQuery

from loader import dp
from states import ReadyToCon


@dp.message_handler(text='ASCII')
async def ascii_message(message: types.Message):
    await message.answer(f'Отлично, теперь отправь изображение')
    await ReadyToCon.awaiting_ascii_photo.set()


@dp.message_handler(text='8-bit')
async def bit_8_message(message: types.Message):
    await message.answer(f'Отлично, теперь отправь изображение')
    await ReadyToCon.awaiting_8_bit_photo.set()


@dp.message_handler(text='8-bit цветное')
async def bit_8_color_message(message: types.Message):
    await message.answer(f'Отлично, теперь отправь изображение')
    await ReadyToCon.awaiting_8_bit_col_photo.set()


@dp.callback_query_handler(text='Отмена')
async def send_message(call: CallbackQuery):
    await FSMContext.finish()
    await call.message.answer('Вы отменили изменение')
