import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "6907074579:AAFJOtvMEDN8ewOVP4XnxOxWyZY-OTjLXXM"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()
start_buttons = [
    KeyboardButton(text="хочу сыграть"),
    KeyboardButton(text="не хочу")
]
kb_builder.row(*start_buttons, width=2)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Привет, хочу предложить тебе сыграть в камень, ножницы, бумага',
        reply_markup=kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    )

@dp.message(F.text.lower().in_(["хочу сыграть", "еще один раунд"]))
async def process_start_command(message: Message):
    builder = ReplyKeyboardBuilder()
    action_buttons = [
        KeyboardButton(text="камень"),
        KeyboardButton(text="ножницы"),
        KeyboardButton(text="бумага")
    ]
    builder.row(*action_buttons, width=3)
    await message.answer(
        text='Выбери свой вариант и нажми на кнопку. Пока думаешь, я подберу свой',
        reply_markup=builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    )

@dp.message(F.text.lower().in_(["не хочу", "мне надоело"]))
async def process_start_command(message: Message):
    await message.answer(
        text='Заходи как будешь готов',
    )


@dp.message(F.text.lower().in_(["камень", "ножницы", "бумага"]))
async def process_start_command(message: Message):
    retry_builder = ReplyKeyboardBuilder()
    retry_buttons = [
        KeyboardButton(text="еще один раунд"),
        KeyboardButton(text="мне надоело"),
    ]
    retry_builder.row(*retry_buttons)
    user_choice = message.text.lower()
    output_pattern = ["камень", "ножницы", "бумага"]
    bot_choice = random.choice(output_pattern)
    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == "камень" and bot_choice == "ножницы") or \
         (user_choice == "ножницы" and bot_choice == "бумага") or \
         (user_choice == "бумага" and bot_choice == "камень"):
        result = "Вы выиграли!"
    else:
        result = "Вы проиграли!"
    await message.answer(
        text=f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n{result}\nПредлагаю сыграть еще раз, не хочешь?",
        reply_markup=retry_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    )



if __name__ == '__main__':
    dp.run_polling(bot)