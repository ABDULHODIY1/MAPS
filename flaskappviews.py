# # import required library
# import webbrowser
# from tkinter import *
#
# # creating root
# root = Tk()
#
# # setting GUI title
# root.title("WebBrowsers")
#
# # setting GUI geometry
# root.geometry("660x660")
#
# # call webbrowser.open() function.
# webbrowser.open("www.instagram.com")
# root.mainloop()
TOKEN = "5898677888:AAFQYDnQY369vIFNZdc5xbyr7QIi_1laado"
ADMIN_IDS = [5640990557]
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor

# TOKEN = "YOUR_BOT_TOKEN"
# ADMIN_IDS = [123456789, 987654321]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id in ADMIN_IDS:
        await message.reply("Salom, admin!", parse_mode=ParseMode.MARKDOWN)
    else:
        await message.reply("Salom, foydalanuvchi!", parse_mode=ParseMode.MARKDOWN)
@dp.message_handler(commands='check')
async def check_admins_online_status():
    me = await bot.me
    for admin_id in ADMIN_IDS:
        admin = await bot.get_chat(admin_id)
        if admin.status == 'online':
            print(f"Admin {admin.username} ({admin_id}) is online")
        else:
            print(f"Admin {admin.username} ({admin_id}) is offline")

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await start(message)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
    check_admins_online_status()
