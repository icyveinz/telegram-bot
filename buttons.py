from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message

TOKEN = "6907074579:AAFJOtvMEDN8ewOVP4XnxOxWyZY-OTjLXXM"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Создаем объекты кнопок
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего кошки боятся больше?',
        reply_markup=keyboard
    )


# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
        reply_markup=ReplyKeyboardRemove()
    )


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше',
        reply_markup=ReplyKeyboardRemove()
    )




if __name__ == '__main__':
    dp.run_polling(bot)