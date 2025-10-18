import os
import logging
import traceback
from pyrogram import Client
from dotenv import load_dotenv


class Katsu:
    def __init__(self):
        load_dotenv()

        self.name = ":memory:"  # use in-memory session (no local .session file)
        self.api_id = int(os.getenv("API_ID"))
        self.api_hash = os.getenv("API_HASH")
        self.bot_token = os.getenv("BOT_TOKEN")
        self.plugins = dict(root="plugins")

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    def run(self):
        logging.info("Starting katsu_Bot")

        try:
            app = Client(
                name=self.name,
                api_id=self.api_id,
                api_hash=self.api_hash,
                bot_token=self.bot_token,
                plugins=self.plugins
            )
            app.run()
        except Exception:
            logging.error("Bot failed to start:")
            logging.error(traceback.format_exc())


if __name__ == "__main__":
    Katsu().run()
