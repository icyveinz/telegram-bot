import random
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "6907074579:AAFJOtvMEDN8ewOVP4XnxOxWyZY-OTjLXXM"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
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
        text=f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n<b>{result}</b>\n<i>Предлагаю сыграть еще раз, не хочешь?</i>",
        reply_markup=retry_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    )



if __name__ == '__main__':
    dp.run_polling(bot)


LEXICON_RU: dict[str, str] = {
    '/start': '<b>Привет!</b>\nДавай с тобой сыграем в игру '
              '"Камень, ножницы, бумага"?\n\nЕсли ты, вдруг, '
              'забыл правила, команда /help тебе поможет!\n\n<b>Играем?</b>',
    '/help': 'Это очень простая игра. Мы одновременно должны '
             'сделать выбор одного из трех предметов. Камень, '
             'ножницы или бумага.\n\nЕсли наш выбор '
             'совпадает - ничья, а в остальных случаях камень '
             'побеждает ножницы, ножницы побеждают бумагу, '
             'а бумага побеждает камень.\n\n<b>Играем?</b>',
    'rock': 'Камень 🗿',
    'paper': 'Бумага 📜',
    'scissors': 'Ножницы ✂',
    'yes_button': 'Давай!',
    'no_button': 'Не хочу!',
    'other_answer': 'Извини, увы, это сообщение мне непонятно...',
    'yes': 'Отлично! Делай свой выбор!',
    'no': 'Жаль...\nЕсли захочешь сыграть, просто разверни '
          'клавиатуру и нажми кнопку "Давай!"',
    'bot_won': 'Я победил!\n\nСыграем еще?',
    'user_won': 'Ты победил! Поздравляю!\n\nДавай сыграем еще?',
    'nobody_won': 'Ничья!\n\nПродолжим?',
    'bot_choice': 'Мой выбор'
}