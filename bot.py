import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from openai import OpenAI

# ENV VARIABLES
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Dive Hook AI\n\n"
        "🔥 Hooks\n✍️ Captions\n#️⃣ Viral Hashtags\n👉 CTA\n\n"
        "👉 Sirf apna TOPIC bhejo"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text

    try:
        prompt = f"""
Generate:
1. 5 viral hooks
2. 1 caption
3. 1 CTA
4. 5 viral hashtags

Topic: {topic}
Language: Hinglish
"""

        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        output = response.output_text.strip()
        await update.message.reply_text(output)

    except Exception as e:
        logging.error(e)
        await update.message.reply_text(
            "❌ Error aa gaya.\nThoda wait karo ya naya topic bhejo."
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        result = response.output_text.strip()

        await wait_msg.delete()
        await update.message.reply_text(result)

    except Exception as e:
        logging.error(e)
        await wait_msg.delete()
        await update.message.reply_text(
            "❌ Error aa gaya.\n"
            "Thoda wait karo ya naya topic bhejo."
        )

# ======================
# MAIN
# ======================
def main():
    app = ApplicationBuilder().token(8252502184:AAGSOXjz1FqQNTgAVk6_cJS9RnU58W5I56k).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Dive Hook AI is running...")
    app.run_polling()

if __name__ == "__main__":
    main()# ===== MAIN =====
def main():
    app = ApplicationBuilder().token(8252502184:AAGSOXjz1FqQNTgAVk6_cJS9RnU58W5I56k).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Dive Hook AI is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
