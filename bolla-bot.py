import logging
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime
import requests
import json

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = "7551900755:AAECNVXBRNK09TY5l25DJ5KW3WQ-D6I5Ie8"
CHAOS_API = "https://chaos-data.projectdiscovery.io/index.json"
BUG_BOUNTY_RADAR_API = "https://raw.githubusercontent.com/kingpaler/bbrf/master/programs.json"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("اهلا بيك يا معلم انا بولا بوت ✌️")

async def new_programs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("⏳ جاري البحث عن أحدث برامج الباك باونتي...")
    chaos_programs = requests.get(CHAOS_API).json()
    radar_programs = requests.get(BUG_BOUNTY_RADAR_API).json()
    result = "🔍 أحدث برامج الباك باونتي:\n"
    for program in chaos_programs[:5]:
        result += f"- {program['name']} ({program['URL']})\n"
    for program in radar_programs[:5]:
        result += f"- {program['program_name']} ({program['url']})\n"
    await update.message.reply_text(result)

async def leaks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🚨 جاري البحث عن التسريبات...")
    # Example placeholder for leaks
    await update.message.reply_text("لم يتم العثور على تسريبات حاليا")

def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("new", new_programs))
    app.add_handler(CommandHandler("leaks", leaks))

    app.run_polling()

if __name__ == "__main__":
    main()
