from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

to_prod_markup = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton('Связь с разработчиком',
                                                               url='https://t.me/AwesomeGeorge')]
                                      ])
