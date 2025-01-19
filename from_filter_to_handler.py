from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message


TOKEN = "6907074579:AAFJOtvMEDN8ewOVP4XnxOxWyZY-OTjLXXM"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

class MyCustomFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
            # Если в списке есть числа - возвращаем словарь со списком чисел по ключу 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False


@dp.message(F.text.lower().startswith('найди'), MyCustomFilter())
async def process_if_no_numbers(message : Message, numbers : list[int]):
    await message.answer(text=f"Я нашел числа : {', '.join(str(num) for num in numbers)}")


@dp.message(F.text.lower().startswith('найди'))
async def process_if_no_numbers(message : Message):
    await message.answer(text="Я не нашел чисел внутри сообщения")


if __name__ == '__main__':
    dp.run_polling(bot)