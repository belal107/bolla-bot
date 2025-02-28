import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7551900755:AAECNVXBRNK09TY5l25DJ5KW3WQ-D6I5Ie8"
BUG_BOUNTY_RADAR_API = "https://raw.githubusercontent.com/bugbounty-radar/changelogs/main/chaos-bugbounty-list.json"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("اهلا بيك يا معلم انا بوله بوت تحت امرك 💪.")

async def new_programs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    radar_response = requests.get(BUG_BOUNTY_RADAR_API)
    if radar_response.headers["Content-Type"] == "application/json":
        radar_programs = radar_response.json()
        message = "🔥 Bug Bounty Radar Latest Programs:\n\n"
        for program in radar_programs[:5]:
            message += f"📌 {program['name']} - {program['url']}\n"
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("API Error: The API did not return JSON data.")
        print("API Error:", radar_response.text)

application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("new", new_programs))

if __name__ == "__main__":
    print("Bolla Bot is running...")
    application.run_polling()
