import os
import logging
from pyrogram import Client
from dotenv import load_dotenv

class Katsu:
    def __init__(self):
        load_dotenv()
        self.name = "katsu_Bot"
        self.api_id = os.getenv("API_ID")
        self.api_hash = os.getenv("API_HASH")
        self.bot_token = os.getenv("BOT_TOKEN")
        self.plugins = dict(root="plugins")
        logging.basicConfig(level=logging.INFO)

    def run(self):
        logging.info(f"Starting {self.name}")
        app = Client(
            self.name,
            api_id=self.api_id,
            api_hash=self.api_hash,
            bot_token=self.bot_token,
            plugins=self.plugins
        )
        app.run()

if __name__ == "__main__":
    try:
        Katsu().run()
    except Exception as e:
        import traceback
        logging.error("Bot failed to start:")
        logging.error(traceback.format_exc())
