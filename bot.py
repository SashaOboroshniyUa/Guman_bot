import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession

from config import BOT_TOKEN as TOKEN
from keyboards import choice_button

HTTP_PROXY_SERVER_ = 'http://proxy.server:3128'

session = AiohttpSession(proxy=('%s' % HTTP_PROXY_SERVER_))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привіт {message.from_user.first_name}, впиши команду /help для всієї информаціі🙂")


@dp.message(Command("help"))
async def get_help(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMWZwVq1gb5W6t8D4dZPBEodBF2Z3UAAq7kMRuLpilITFBNbHT2DNwBAAMCAANtAAM2B"
                                     "A",
                               caption="Цей бот зроблен для того щоб люди не велися на фейкові фонди для допомоги ЗСУ "
                                       "та фейкові благодійні фонди. Тому я зробив самостійно список благодійних фондів"
                                       " яким можна вірити.",
                               reply_markup=choice_button)


@dp.message(F.text == "Підтримка Військових")
async def replay_help_one(message: Message):
    await message.answer("Всі фонди для підтримки військових:\n"
                         "https://savelife.in.ua/\n\n Офіційний фонд підтримки військових\n"
                         "https://prytulafoundation.org/\n\n Офіційний фонд Сергія Притули "
                         "збору грошей для військових\n"
                         "https://www.razomforukraine.org/\n\n Популярний фонд для підтримки людей у яких немає "
                         "будівлі")


@dp.message(F.text == "Підтримка Тварин")
async def replay_help_two(message: Message):
    await message.answer("Всі фонди для підтримки тварин:\n"
                         "https://happypaw.ua/\n\n Фонд підтримки різноманітних тварин\n"
                         "https://uanimals.org/en/\n\n Дуже популярний Український фонд\n"
                         "https://www.savepetsofukraine.kormotech.com/\n\n Фонд що допомогає тваринам "
                         "та робе фотозвіт що допомагають тваринам")


@dp.message(F.text == "Ідеї")
async def ideas(message: Message):
    await message.answer("Якщо в вас є ідеї щоб щось додати то пишить мені, завжди буду радий класним ідеям):\n\n"
                         "@Aboba3393")


async def main():
    bot = Bot(token=TOKEN, session=session, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
