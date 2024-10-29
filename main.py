from loguru import logger
from src.bot import dp, bot

if __name__ == "__main__":
    logger.info("Starting...")
    dp.run_polling(
        bot,
        allowed_updates=[
            "callback_query",
            "business_message",
            "edited_business_message",
            "deleted_business_messages",
        ],
    )
