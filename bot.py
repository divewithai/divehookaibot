import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from openai import OpenAI

# LOGGING
logging.basicConfig(level=logging.INFO)

# ENV VARIABLES
BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

client = OpenAI(api_key=OPENAI_KEY)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 *Welcome to Dive Hook AI*\n\n"
        "Main tumhara personal AI hoon jo Instagram Reels & YouTube Shorts ke liye:\n"
        "🔥 Hooks\n✍️ Captions\n#️⃣ Hashtags\n👉 CTA\n\n"
        "👉 *Sirf apna TOPIC bhejo*\n"
        "Example: AI se paisa kaise kamaye",
        parse_mode="Markdown"
    )

# Handle normal messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text

    await update.message.reply_text("⚡ Content generate ho raha hai...")

    prompt = f"""
Tum ek viral short-form content expert ho.

Topic: {topic}

Output STRICTLY is format me do:

🔥 3 Killer Hooks
✍️ 1 Reel Caption
#️⃣ 5 Viral Hashtags
👉 1 Strong CTA

Language: Hinglish (Roman Hindi)
Tone: Bold, Viral, Creator-focused
"""

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        output = response.output_text.strip()

        await update.message.reply_text(output)

    except Exception as e:
        logging.error(e)
        await update.message.reply_text(
            "❌ Error aaya hai.\n"
            "Thoda wait karo ya naya topic bhejo."
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Dive Hook AI is running...")
    app.run_polling()

if __name__ == "__main__":
    main()        model="gpt-5-mini",
        input=prompt
    )

    text = response.output_text
    await update.message.reply_text(text)

# App start
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("viral", viral))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

app.run_polling()
