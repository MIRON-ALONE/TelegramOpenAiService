import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("Начало выполнения")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("def hello выполнено")
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def main():
    print('main выполнено')
    app = ApplicationBuilder().token("7616064677:AAHzFDKNoB5Qo8hrz33oEeQlsF7jRO5jSFk").build()
    app.add_handler(CommandHandler("hello", hello))
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
