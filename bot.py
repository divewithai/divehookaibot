try:
        prompt = f"""
Generate the following for Instagram Reels / YouTube Shorts:

1. 5 viral hooks
2. 1 engaging caption
3. 1 strong CTA
4. 5 viral hashtags

Topic: {topic}
Language: Hinglish
"""

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

        if not output.strip():
            raise ValueError("Empty response from OpenAI")

        await update.message.reply_text(output.strip())

    except Exception as e:
        logging.exception(e)
        await update.message.reply_text(
            "❌ Error aa gaya.\nThoda wait karo ya naya topic bhejo."
        )
        def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Dive Hook AI is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
