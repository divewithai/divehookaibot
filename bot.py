from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
from openai import OpenAI

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

client = OpenAI(api_key=OPENAI_KEY)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 *Welcome to Dive Hook AI*\n\n"
        "Main tumhara personal AI hoon jo Instagram Reels & YouTube Shorts ke liye:\n"
        "🔥 Hooks\n✍️ Captions\n#️⃣ Hashtags\n👉 CTA banata hoon\n\n"
        "👉 Sirf apna TOPIC bhejo\n"
        "_Example:_ AI se paisa kaise kamaye",
        parse_mode="Markdown"
    )

# /help
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 *Available Commands*\n\n"
        "/start – Bot shuru karo\n"
        "/help – Guide\n"
        "/viral – Full viral content\n\n"
        "Ya sirf topic bhejo 🔥",
        parse_mode="Markdown"
    )

# /viral
async def viral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args)
    if not topic:
        await update.message.reply_text("❌ Topic missing hai.\nExample:\n/viral AI se paisa kaise kamaye")
        return

    await generate_content(update, topic)

# Text handler
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text
    await generate_content(update, topic)

# Core AI function
async def generate_content(update, topic):
    await update.message.reply_text("⚡ Content generate ho raha hai...")

    prompt = f"""
Tum ek viral short-form content expert ho.

Topic: {topic}

Output do:
1. 3 killer hooks (short & powerful)
2. 1 reel caption
3. 5 viral hashtags
4. 1 strong CTA

Language: Hinglish (Roman Hindi)
Tone: Bold, confident, creator-style
"""

    response = client.responses.create(
        model="gpt-5-mini",
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
