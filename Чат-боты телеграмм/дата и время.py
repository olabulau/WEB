import logging
from telegram.ext import Application, CommandHandler
import datetime
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


async def address(update, context):
    await update.message.reply_text(
        "Адрес: г. Ликино-Дулево, ул. Октябрьская, 16")


async def phone(update, context):
    await update.message.reply_text("Телефон: +7(967)060-91-14")


async def site(update, context):
    await update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")


async def work_time(update, context):
    await update.message.reply_text(
        "Время работы: никогда.")


async def time(update, context):
    await update.message.reply_text(f"{datetime.datetime.now().time()}")


async def data(update, context):
    await update.message.reply_text(f"{datetime.datetime.now().date()}")


def main():
    application = Application.builder().token("6114192113:AAHInPMhXptu5PWdYPWMKxJkeAoRxNZUJtI").build()
    application.add_handler(CommandHandler("address", address))
    application.add_handler(CommandHandler("phone", phone))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("work_time", work_time))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("time", time))
    application.add_handler(CommandHandler("data", data))
    application.run_polling()


if __name__ == '__main__':
    main()
