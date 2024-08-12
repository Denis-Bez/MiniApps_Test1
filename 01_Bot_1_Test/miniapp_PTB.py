# Вставьте ваш токен, полученный у BotFather
TOKEN = '5622410166:AAHh6OVhMyDuMkbMwyNmKRlsNbUGpJqJo6A'
# URL вашего mini app
MINI_APP_URL = 'https://denis-bez.github.io/vanilla-js-boilerplate/'

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение с кнопкой для запуска mini app."""
    keyboard = [
        [InlineKeyboardButton("Запустить Mini App", web_app={"url": MINI_APP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Нажмите кнопку, чтобы запустить Mini App:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает нажатие кнопки."""
    query = update.callback_query
    await query.answer()

def main() -> None:
    """Запускает бота."""
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()


