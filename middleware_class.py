from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class SomeMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        # ...
        # Здесь выполняется код на входе в middleware
        # ...

        result = await handler(event, data)

        # ...
        # Здесь выполняется код на выходе из middleware
        # ...

        return result


# В целом, структура не очень сложная. Важно соблюдать следующие требования:
#
#   Пользовательские миддлвари должны наследоваться от класса BaseMiddleware.
#   У пользовательской миддлвари должен быть обязательно реализован асинхронный метод __call__.
#   Метод __call__ всегда принимает 4 обязательных аргумента:
#       self - ссылка на экземпляр класса. Это ООП, друзья.
#       handler - объект хэндлера. Для outer middleware он не определен, потому что пока не пройдены фильтры мы не знаем есть ли вообще подходящий для данного апдейта хэндлер.
#       event - TelegramObject - тип события, которое хотим обработать (Update, Message, CallbackQuery...).
#       data - словарь с данными, ассоциированными с текущим апдейтом.
#   До строчки result = await handler(event, data) можно писать код, который будет выполнен на входе в миддлварь - до принятия решения пропустить апдейт дальше по цепочке в сторону возможного обработчика или дропнуть здесь.
#   Сама строчка result = await handler(event, data) отвечает за то пропустить апдейт дальше или дропнуть. Тут есть нюансы, будем разбирать подробно.
#   После строчки result = await handler(event, data) можно писать код, который будет выполнен на выходе из миддлвари, независимо от того дошел апдейт до хэндлера (или даже просто до следующей миддлвари) или нет.
#   Строчка return result, чтобы пропустить апдейт в следующий роутер или просто return, чтобы не пропустить. Тоже разберемся.
