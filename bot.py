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

# ===== CONFIG =====
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)

# ===== COMMANDS =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Dive Hook AI\n\n"
        "Sirf apna TOPIC bhejo aur main bana dunga:\n"
        "🔥 Hooks\n📝 Captions\n#️⃣ Hashtags\n👉 CTA\n\n"
        "Example:\nAI se paisa kaise kamaye"
    )

# ===== MESSAGE HANDLER =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text

    await update.message.reply_text("⚡ Content generate ho raha hai...")

    prompt = f"""
You are a viral content expert.
Create Instagram Reels / YouTube Shorts content for this topic:

Topic: {topic}

Give output in this format ONLY:

🔥 Hooks (3 short hooks)
📝 Caption (1 powerful caption)
#️⃣ Hashtags (8–10 viral hashtags)
👉 CTA (1 strong CTA)

Use Hinglish.
"""

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt,
        )

        output = response.output_text.strip()
        await update.message.reply_text(output)

    except Exception as e:
        logging.error(e)
        await update.message.reply_text(
            "❌ Error aaya hai.\nThoda wait karo ya naya topic bhejo."
        )

# ===== MAIN =====
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Dive Hook AI is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
