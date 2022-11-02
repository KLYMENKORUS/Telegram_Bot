import json, string
from aiogram import types
from create_bot import dp, Dispatcher


async def echo_send(message: types.Message):
    if message.text == 'Привет' or 'привет':
        await message.answer(f'И тебе привет, {message.from_user.first_name}!')

    elif {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply(f'Маты запрещены, {message.from_user.first_name}')
        await message.delete()


def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
