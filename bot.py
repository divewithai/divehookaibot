import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from openai import OpenAI

# ========================
# ENV VARIABLES
# ========================
BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

client = OpenAI(api_key=OPENAI_KEY)

# ========================
# /start COMMAND
# ========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 *Welcome to Dive Hook AI*\n\n"
        "Main tumhara personal AI assistant hoon jo:\n"
        "• Viral Hooks\n"
        "• Reel Captions\n"
        "• Smart Hashtags\n"
        "• Strong CTA\n\n"
        "👉 *Sirf apna TOPIC bhejo*\n"
        "Example:\nAI se paisa kaise kamaye\n\n"
        "Ready? Topic bhejo 👇",
        parse_mode="Markdown"
    )

# ========================
# HANDLE USER MESSAGE
# ========================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text

    await update.message.reply_text("⚡ Content generate ho raha hai...")

    try:
        prompt = f"""
Tum ek viral short-form content expert ho.

Topic: {topic}

Output strict format me do:
1. 3 killer hooks
2. 1 reel caption
3. 5 viral hashtags
4. 1 strong CTA

Language: Hinglish (Roman Hindi)
Tone: Bold, creator-focused, Indian audience
"""

        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt,
        )

        result = response.output_text.strip()

        await update.message.reply_text(result)

    except Exception as e:
        await update.message.reply_text(
            "❌ Kuch error aaya hai.\n"
            "Thoda baad try karo ya admin ko batao."
        )
        print("ERROR:", e)

# ========================
# MAIN APP
# ========================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Dive Hook AI is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
