from vkbottle.bot import Bot, BotLabeler

from config import Config
import asyncio
import logging

from handlers import main_labeler


async def main() -> None:
    labeler = BotLabeler()
    labeler.load(main_labeler)
    bot = Bot(token=Config.TOKEN, labeler=labeler)
    
    await bot.run_polling()
    

if __name__ == "__main__":
    logging.getLogger("vkbottle").setLevel(logging.INFO)
    asyncio.run(main())