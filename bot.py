import asyncio
import logging
from data import config

from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

import handlers
from utils.notify_admins import notify_admins
from utils.set_bot_commands import set_bot_commands

# Bot obyekti yaratish, tokenni config faylidan olish
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()  # Xotira saqlash
dp = Dispatcher(storage=storage)  # Dispatcher yaratish

async def main():
    """
    Asosiy funktsiya, botni ishga tushurish va handlerlarni sozlash
    """
    handlers.setup(dp)  # Handlerlarni ulash
    await set_bot_commands(bot)
    await notify_admins(bot)
    await bot.delete_webhook(drop_pending_updates=True)  # Webhookni o'chirish va kutayotgan yangilanishlarni olib tashlash
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())  # Botni pollingga boshlash

if __name__ == "__main__":
    # Loggerni sozlash
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
                "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Bot ishga tushmoqda")
    try:
        asyncio.run(main())  # Asosiy funktsiyani ishga tushurish
    except (KeyboardInterrupt, SystemExit):  # Foydalanuvchi botni to'xtatganida
        logger.info("Bot to'xtatildi")
    finally:
        # Bot sessiyasini tozalash
        asyncio.run(bot.session.close())  # Bot sessiyasini yopish
