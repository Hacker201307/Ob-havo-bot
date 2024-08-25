import logging
from aiogram import Bot, Dispatcher, executor, types
from ob_havo import malumot, but

API_TOKEN='7310918137:AAF2rZZy8WEwGppuyxsHV5TC8uiAGzDTu3I'# Configure logginglogging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start(msg: types.Message):
    await msg.answer(f'Assalomu alekum hurmatli {msg.from_user.full_name} Ob havo botga xush kelibsiz shaxarni tanlang', reply_markup=but)

@dp.message_handler()
async def nomi(msg: types.Message):
    url = 'https://ob-havo.me/uploads/ob-havo-fon.webp'
    await bot.send_photo(msg.chat.id, photo=url, caption=malumot(msg.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

