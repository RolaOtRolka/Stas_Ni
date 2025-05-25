from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Г. Москва ул. Пушкина д. Калатушкина', callback_data='addresses_1'),
        InlineKeyboardButton(text='Г. Минск ул. Немига д. 42', callback_data='addresses_2'),
        InlineKeyboardButton(text='Г. Варшава ул. Стефана Баторего д. 43', callback_data='addresses_3'),
        width=2
    )

    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='сайт', url='https://www.porsche.com/central-eastern-europe/ru/'),
            InlineKeyboardButton(text='телеграмм', url='tg://resolve?domain=Rola_ot_rolka')
         ]
    ]
)
