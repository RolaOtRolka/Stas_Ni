from aiogram import types, Router, F
from aiogram.types import FSInputFile


catalog_router = Router()


@catalog_router.message(F.text == 'Daewoo Matiz')
async def product_1(message: types.Message):
    photo = FSInputFile(r'img\catalog\Daewoo_Matiz.jpg')
    await message.answer_photo(photo=photo, caption='Автомобиль Матиз')


@catalog_router.message(F.text == 'BMW E34')
async def product_2(message: types.Message):
    photo = FSInputFile(r'img\catalog\BMW _E34.jpg')
    await message.answer_photo(photo, caption='Автомобиль БМВ')


@catalog_router.message(F.text == 'Boeing 737')
async def product_3(message: types.Message):
    photo = FSInputFile(r'img\catalog\boeing_737.jpg')
    await message.answer_photo(photo, caption='Самолет Боинг')


@catalog_router.message(F.text == 'Lamborgini Urus')
async def product_4(message: types.Message):
    photo = FSInputFile(r'img\catalog\Lamborgini_Urus.jpg')
    await message.answer_photo(photo, caption='Автомобиль Урус')


@catalog_router.message(F.text == 'Ferrari F40')
async def product_5(message: types.Message):
    photo = FSInputFile(r'img\catalog\F40.jpg')
    await message.answer_photo(photo, caption='Автомобиль Ф40')


@catalog_router.message(F.text == 'Porshe 911')
async def product_6(message: types.Message):
    photo = FSInputFile(r'img\catalog\Porshe_911.jpg')
    await message.answer_photo(photo, caption='Автомобиль 911')