from idlelib.query import Query

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Добро пожаловать в мир автопокупок с нашим виртуальным помощником! \n \n Этот умный бот поможет вам легко найти идеальный автомобиль. Он предоставляет актуальные предложения, сравнивает цены и отвечает на все ваши вопросы о характеристиках . С ним процесс покупки станет простым и увлекательным! \n \n Давайте начнем ваше автомобильное путешествие вместе!', reply_markup=reply.main_kb)


@user_router.message(F.text.lower() == 'каталог🚘')
@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer('Каталог товаров', reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower() == 'про нас🤫')
@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('Бот для продажи авто по Беларуси', reply_markup=inline.links_kb)


@user_router.message(F.text.lower() == 'контакт📱')
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer('''Контакты: +375339009914''')

#     await message.answer('''tagy HTML
#
# <b>Жирный</b>
# <i>Курсив</i>
# <u>Подчеркнутый</u>
# <s>Зачеркнутый</s>
# <tg-spoiler>Спойлер</tg-spoiler>
# <a href='https://www.porsche.com/central-eastern-europe/ru/'>Сыллка</a>
# <code>Код</code>
# <pre>Стаснислав Ничипор</pre>
# ''')


@user_router.message(F.text.lower() == 'адрес🗺')
@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer('наши адреса:', reply_markup=inline.addresses_kb())


@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_info(callback:types.CallbackQuery):
    query = callback.data.split('_')[1]
    if query == '1':
        await callback.message.answer('Здание находиться рядом с Кремлем \nГ. Москва ул. Пушкина д. Калатушкина')
    elif query == '2':
        await callback.message.answer('''Выходите из стании метро Немига, идете прямо, на лево и рядом с ТЦ Галерея будет вход в автосалон \n Г. Минск ул. Немига д. 42''')
    else:
        await callback.message.answer('Выходите из стании метро Brodno, идете прямо и там будет наш автосалон \n Г. Варшава ул. Стефана Баторего д. 43')
    await callback.answer('Адрес отправлен')


@user_router.message(F.text.lower() == 'назад')
async def back_menu(message: types.Message):
    await message.answer('Главное меню', reply_markup=reply.main_kb)


# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == 'доставка')
# @user_router.message(F.text.lower().contains('доставк'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().startswith('как'), F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().contains('цен') | F.text.lower().contains('стоимост'))
async def echo(message: types.Message):
    await message.answer('Бот пока находится в разработке')
 #  user_text = message.text
 # await message.answer(user_text)