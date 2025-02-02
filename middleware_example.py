from aiogram import types, Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Update
from aiogram.dispatcher.middlewares.base import BaseMiddleware

TOKEN = "6907074579:AAFJOtvMEDN8ewOVP4XnxOxWyZY-OTjLXXM"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict):
        if event.message:
            print(f"Получено сообщение: {event.message.text}")
        return await handler(event, data)

# Подключаем middleware
dp.update.middleware(LoggingMiddleware())

# Обработчик команды /start
@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Привет! Я твой бот.")

if __name__ == '__main__':
    dp.run_polling(bot)
