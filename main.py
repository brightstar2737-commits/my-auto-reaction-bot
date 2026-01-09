import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReactionTypeEmoji
from aiohttp import web

# Token ကို ဒီမှာထည့်ပါ
API_TOKEN = '8282678322:AAFry45oBkxy2wb6_nmte4_lhZo1g4h8XBw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.channel_post()
async def auto_reaction(message: types.Message):
    try:
        await message.react(reaction=[ReactionTypeEmoji(emoji="❤️")])
    except Exception as e:
        print(f"Error: {e}")

# Render အတွက် Dummy Web Server ဆောက်ခြင်း (Sleep မဖြစ်စေရန်)
async def handle(request):
    return web.Response(text="Bot is Running!")

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    
    # Web server နဲ့ Bot ကို ပြိုင်တူ run ရန်
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT', 10000)))
    await site.start()
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
