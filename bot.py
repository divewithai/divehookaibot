from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import openai
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

openai.api_key = OPENAI_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Dive Hook AI\n\n"
        "Main tumhara personal AI assistant hoon jo\n"
        "Instagram Reels & YouTube Shorts ke liye\n"
        "viral hooks, captions, hashtags aur CTA banata hai.\n\n"
        "👉 Sirf apna TOPIC bhejo\n"
        "Example:\n"
        "AI se paisa kaise kamaye\n\n"
        "Ready? Topic bhejo 👇"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text

    prompt = f"""
Tum ek viral short-form content expert ho.

Topic: {topic}

Output do:
1. 3 killer hooks
2. 1 reel caption
3. 5 relevant hashtags
4. 1 strong CTA

Language: Hinglish (Roman Hindi)
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    await update.message.reply_text(response.choices[0].message.content)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling(await update.message.reply_text(
    "🚀 Welcome to Dive Hook AI\n\n"
    "Main tumhara personal AI assistant hoon jo\n"
    "Instagram Reels & YouTube Shorts ke liye\n"
    "viral hooks, captions, hashtags aur CTA banata hai.\n\n"
    "👉 Sirf apna TOPIC bhejo\n"
    "Example:\n"
    "AI se paisa kaise kamaye\n\n"
    "Ready? Topic bhejo 👇"
)
