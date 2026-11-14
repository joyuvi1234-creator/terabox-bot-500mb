import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN", "").strip()
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "").strip()
OWNER_ID = int(os.getenv("OWNER", "0"))
PORT = int(os.getenv("PORT", "8000"))
TERABOX_API_DOWNLOAD_ENDPOINT = os.getenv(
    "TERABOX_API_DOWNLOAD_ENDPOINT",
    "https://terabox-api.mn-bots.workers.dev/download"
).strip()
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "500"))
