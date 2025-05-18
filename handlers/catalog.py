from aiogram import types, Router, F
from aiogram.types import FSInputFile


catalog_router = Router()


@catalog_router.message(F.text == 'Daewoo Matiz')
async def product_1(message: types.Message):
    photo = FSInputFile(r'img\catalog\Daewoo_Matiz.jpg')
    text = '''Daewoo Matiz
    
Daewoo Matiz — это компактный городской автомобиль, который был представлен в 1998 году и стал популярным благодаря своей экономичности и маневренности. Он оснащен небольшими, но эффективными двигателями, что делает его идеальным выбором для городских условий. Удобный интерьер и доступная цена сделали Matiz привлекательным вариантом для молодых водителей и семей.
    
цена: 1850 долларов '''
    await message.answer_photo(photo=photo, caption=text)


@catalog_router.message(F.text == 'BMW E34')
async def product_2(message: types.Message):
    photo = FSInputFile(r'img\catalog\BMW _E34.jpg')
    text = '''BMW E34
    
BMW E34 — это модель пятого поколения BMW 5 Series, производившаяся с 1987 по 1996 годы. Она известна своим элегантным дизайном, высоким уровнем комфорта и отличной управляемостью, что делает ее популярной как среди любителей автомобилей, так и среди семей. E34 предлагалась с разнообразными бензиновыми и дизельными двигателями, обеспечивая хороший баланс между производительностью и экономичностью.

цена: 2700 долларов'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text == 'Boeing 737')
async def product_3(message: types.Message):
    photo = FSInputFile(r'img\catalog\boeing_737.jpg')
    text = '''Boeing 737
Boeing 737 — это узкофюзеляжный реактивный самолет, разработанный компанией Boeing, который впервые совершил полет в 1967 году. Он стал одним из самых популярных и широко используемых коммерческих авиалайнеров в мире, предлагая различные модификации для коротких и средних дистанций. Благодаря своей надежности, экономичности и комфортабельности Boeing 737 используется многими авиакомпаниями для пассажирских и грузовых перевозок.

цена: 112,6 миллионов долларов'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text == 'Lamborgini Urus')
async def product_4(message: types.Message):
    photo = FSInputFile(r'img\catalog\Lamborgini_Urus.jpg')
    text = '''Lamborgini Urus

Lamborghini Urus — это высокопроизводительный внедорожник, который сочетает в себе элегантный дизайн и мощные характеристики. Оснащенный 4,0-литровым V8 с двойным турбонаддувом, Urus способен разгоняться до 100 км/ч менее чем за 3,6 секунды, обеспечивая захватывающие впечатления от вождения. Интерьер автомобиля сочетает роскошь и современные технологии, предлагая водителю и пассажирам высокий уровень комфорта и удобства.

цена: 190 млн долларов
'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text == 'Ferrari F40')
async def product_5(message: types.Message):
    photo = FSInputFile(r'img\catalog\F40.jpg')
    text = '''Ferrari F40

Ferrari F40 — это культовой суперкар, выпущенный в 1987 году в честь 40-летия компании Ferrari. Оснащенный 2,9-литровым V8 с двойным турбонаддувом, он способен развивать скорость до 320 км/ч и разгоняться до 100 км/ч всего за 3,8 секунды. С минималистичным дизайном и акцентом на производительность, F40 стал символом эпохи и остается одним из самых желанных автомобилей среди коллекционеров.

цена: 2 млн долларов
'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text == 'Porshe 911')
async def product_6(message: types.Message):
    photo = FSInputFile(r'img\catalog\Porshe_911.jpg')
    text = '''Porshe 911

Porsche 911 — это легендарный спортивный автомобиль, впервые представленный в 1964 году, который сочетает в себе элегантный дизайн и выдающиеся характеристики. С задним расположением двигателя и характерной формой кузова, 911 предлагает отличную управляемость и динамику на дороге. Благодаря разнообразию модификаций и мощным двигателям, этот автомобиль продолжает оставаться иконой среди любителей скорости и стиля.

цена: 90 тыс долларов
'''
    await message.answer_photo(photo, caption=text)