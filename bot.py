import logging
import threading
from flask import Flask
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH, OWNER_ID, PORT

logging.basicConfig(level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

app = Flask(__name__)

@app.route("/")
def health():
    return "TeraBox bot is running."

def run_health_server():
    app.run(host="0.0.0.0", port=PORT)

class TeraBoxBot(Client):
    def __init__(self):
        super().__init__(
            "terabox-bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"},
            workers=8,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        logging.info("Bot started as @%s", me.username)
        if OWNER_ID:
            try:
                await self.send_message(OWNER_ID, f"{me.first_name} is online.")
            except Exception:
                logging.exception("Could not send startup message to owner")

if __name__ == "__main__":
    if not BOT_TOKEN or not API_ID or not API_HASH:
        raise SystemExit("Set TOKEN, API_ID and API_HASH environment variables.")
    threading.Thread(target=run_health_server, daemon=True).start()
    TeraBoxBot().run()
