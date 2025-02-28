import os
import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("7551900755:AAECNVXBRNK09TY5l25DJ5KW3WQ-D6I5Ie8")
CHAOS_API = "https://chaos-data.projectdiscovery.io/index.json"
BUG_BOUNTY_RADAR_API = "https://bugbountyradar.io/api/programs" 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hey Bolla! Bot is running ✅")

async def new_programs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        radar_response = requests.get(BUG_BOUNTY_RADAR_API)
        radar_programs = radar_response.json() if radar_response.headers['Content-Type'].startswith('application/json') else []
        radar_text = '\n'.join([program['name'] for program in radar_programs[:10]]) if radar_programs else "No programs available from Bug Bounty Radar."
    except Exception as e:
        radar_text = f"Error fetching Bug Bounty Radar programs: {str(e)}"

    try:
        chaos_response = requests.get(CHAOS_API)
        chaos_programs = chaos_response.json() if chaos_response.headers['Content-Type'].startswith('application/json') else []
        chaos_text = '\n'.join([program['name'] for program in chaos_programs[:10]]) if chaos_programs else "No programs available from Chaos."
    except Exception as e:
        chaos_text = f"Error fetching Chaos programs: {str(e)}"

    message = f"Bug Bounty Radar Programs:\n{radar_text}\n\nChaos Programs:\n{chaos_text}"
    await update.message.reply_text(message)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("new", new_programs))

    logging.info("Application started")
    app.run_polling()
