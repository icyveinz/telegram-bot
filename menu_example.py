import random
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, KeyboardButtonPollType, \
    BotCommand
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "6907074579:AAFJOtvMEDN8ewOVP4XnxOxWyZY-OTjLXXM"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')
    ]
    await bot.set_my_commands(main_menu_commands)

@dp.message(F.text.lower().in_(["/help"]))
async def show_help(message: Message):
    await message.reply(text=LEXICON_RU['/help'])




if __name__ == '__main__':
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    dp.startup.register(set_main_menu)
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