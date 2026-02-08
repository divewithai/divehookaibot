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

# ======================
# CONFIG
# ======================
BOT_TOKEN = os.getenv(8252502184:AAGSOXjz1FqQNTgAVk6_cJS9RnU58W5I56k)
OPENAI_API_KEY = os.getenv(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)

client = OpenAI(api_key=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)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ======================
# START COMMAND
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 *Welcome to Dive Hook AI*\n\n"
        "Main tumhara personal AI hoon jo:\n"
        "🔥 Hooks\n"
        "✍️ Captions\n"
        "#️⃣ Viral Hashtags\n"
        "👉 CTA\n\n"
        "banata hoon Instagram Reels & YouTube Shorts ke liye.\n\n"
        "👉 *Sirf apna TOPIC bhejo*",
        parse_mode="Markdown"
    )

# ======================
# HANDLE MESSAGE
# ======================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text

    wait_msg = await update.message.reply_text("⚡ Content generate ho raha hai...")

    prompt = f"""
Tum ek expert social media strategist ho.

Topic: {topic}

Output strictly is format me do:

🔥 HOOKS (5 short powerful hooks)

✍️ CAPTIONS (2 captions)

👉 CTA (1 strong CTA)

#️⃣ VIRAL HASHTAGS (10 hashtags)

Language: Hinglish
Tone: Viral, confident, creator-focused
"""

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
