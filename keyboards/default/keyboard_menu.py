from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ASCII'),
            KeyboardButton(text='8-bit'),
        ]
    ],
    resize_keyboard=True
)
