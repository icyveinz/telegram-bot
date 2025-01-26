from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "6907074579:AAFJOtvMEDN8ewOVP4XnxOxWyZY-OTjLXXM"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


kb_builder = ReplyKeyboardBuilder()

contact_button = KeyboardButton(text='Send Contact', request_contact=True)
geo_button = KeyboardButton(text='Send Location', request_location=True)
poll_btn = KeyboardButton(text='Send Poll', request_poll=KeyboardButtonPollType())

kb_builder.row(contact_button, geo_button, poll_btn, width=1)

keyboard = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Testing',
        reply_markup=keyboard
    )



if __name__ == '__main__':
    dp.run_polling(bot)