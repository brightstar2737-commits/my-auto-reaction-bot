import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReactionTypeEmoji

# 8282678322:AAFry45oBkxy2wb6_nmte4_lhZo1g4h8XBw
API_TOKEN = '8282678322:AAFry45oBkxy2wb6_nmte4_lhZo1g4h8XBw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.channel_post()
async def auto_reaction(message: types.Message):
    try:
        # ❤️ reaction တစ်ခုတည်း ပေးရန်
        await message.react(reaction=[ReactionTypeEmoji(emoji="❤️")])
    except Exception as e:
        print(f"Error: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
  
