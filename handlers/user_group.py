from aiogram import types, Router, F

group_router = Router()

restricted_words = ['корова', 'коза', 'мука', 'тюрьма']

@group_router.message(F.text)
async def cleaner(message: types.Message):
    words_lst = message.text.split(' ')
    for word in words_lst:
        if word.lower() in restricted_words:
            # await message.answer(f'{message.from_user.first_name} соблюдайте правила чата')
            await message.answer(f'@{message.from_user.username} соблюдайте правила чата')
            await message.delete()
            break