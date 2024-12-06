from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("Начало выполнения")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("def hello выполнено")
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start_telegram_bot():
    print('main выполнено')
    app = ApplicationBuilder().token("YOUR_TOKEN_HERE").build()
    app.add_handler(CommandHandler("hello", hello))
    await app.run_polling()

