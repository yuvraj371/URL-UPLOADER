import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6526489669:AAFsAPfhjPFsh3es802LPzN9zbVTmvLi5Fc")

    API_ID = int(os.environ.get("API_ID", "11479687"))

    API_HASH = os.environ.get("API_HASH", "424be8d526b7df9d2614e2bafff47c81")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6390672120").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Infinity_XBotz")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @url_uploaderV3Bott"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Autodeletebot:Dharamveer1100@cluster0.luyy59m.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "TG_FILES")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002096246448"))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "6390672120"))
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Url_Uploader_Infinity_Bot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))

    PRO_USERS.append(OWNER_ID)

    DATABASE_NAME = os.environ.get("database_name", " autodeletebot")

    PORT = os.environ.get ("PORT", '8112')
