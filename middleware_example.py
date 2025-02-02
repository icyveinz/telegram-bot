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


# Где можно использовать Middleware?
#
#     Логирование: Записывать все входящие сообщения или действия пользователей.
#
#     Проверка прав доступа: Проверять, имеет ли пользователь право на выполнение определенных команд.
#
#     Фильтрация данных: Очищать или проверять данные перед их обработкой.
#
#     Учет статистики: Собирать данные о действиях пользователей для анализа.
#
#     Кэширование: Сохранять часто запрашиваемые данные, чтобы уменьшить нагрузку на сервер.
#
# Как это работает в коде:
#
#     on_pre_process_update: Вызывается перед тем, как сообщение попадет в обработчик. Здесь можно выполнить предварительную обработку.
#
#     on_post_process_update: Вызывается после того, как сообщение обработано. Здесь можно выполнить дополнительные действия, например, отправить уведомление.
#
# Преимущества использования Middleware:
#
#     Упрощение кода: Не нужно дублировать код в каждом обработчике.
#
#     Гибкость: Можно легко добавлять или удалять функциональность.
#
#     Масштабируемость: Легко добавлять новые middleware по мере роста проекта.