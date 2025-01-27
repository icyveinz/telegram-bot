from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, BotCommand

LEXICON_RU: dict[str, str] = {
    '/start': 'Это пример бота, в котором есть меню с пунктами для отображения пользователю',
    '/help': 'Заходи в репозиторий на ГИТЕ https://github.com/icyveinz/telegram-bot',
}

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


@dp.message(F.text.lower().in_(["/start"]))
async def show_help(message: Message):
    await message.reply(text=LEXICON_RU['/start'])

# Этот хэндлер будет срабатывать на команду "/delmenu"
# и удалять кнопку Menu c командами
@dp.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')




if __name__ == '__main__':
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)