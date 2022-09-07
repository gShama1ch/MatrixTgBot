from aiogram.dispatcher.filters.state import StatesGroup, State


class ReadyToCon(StatesGroup):
    awaiting_ascii_photo = State()
    awaiting_8_bit_photo = State()
    awaiting_8_bit_col_photo = State()
