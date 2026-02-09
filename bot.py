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

# ================= CONFIG =================
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Dive Hook AI\n\n"
        "Main tumhara personal AI hoon jo:\n"
        "🔥 Hooks\n✍️ Captions\n#️⃣ Viral Hashtags\n👉 CTA\n\n"
        "banata hoon Instagram Reels & YouTube Shorts ke liye.\n\n"
        "👉 Sirf apna TOPIC bhejo"
    )

# ================= MESSAGE HANDLER =================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text

    prompt = f"""
Create content for Instagram Reels / YouTube Shorts.

Topic: {topic}
Language: Hinglish

Give:
1. 5 viral hooks
2. 1 engaging caption
3. 1 strong CTA
4. 5 viral hashtags
"""

    try:
        response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
        )
        output = ""
        for item in response.output:
            if item["type"] == "message":
                for content in item["content"]:
                    if content["type"] == "output_text":
                        output += content["text"]

        await update.message.reply_text(output.strip())

    except Exception as e:
    logging.exception(e)
    await update.message.reply_text(
        "❌ Error aa gaya.\nThoda wait karo ya naya topic bhejo."
    )
# ================= MAIN =================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Dive Hook AI is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
