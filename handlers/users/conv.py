from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from loader import dp, bot
from states import ReadyToCon





@dp.message_handler(content_types=['photo'], state=ReadyToCon.awaiting_8_bit_photo)
async def convert_to_ascii(message: types.Message, state: FSMContext):
    print(message.photo[0].file_id)
    await message.answer("Пока так")
    await state.finish()


@dp.message_handler(content_types=['photo'], state=ReadyToCon.awaiting_8_bit_col_photo)
async def convert_to_ascii(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, message.photo[0].file_id)
    print(message.photo[0].file_id)
    await message.answer("Пока так")
    await state.finish()
