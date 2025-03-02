from logging import getLogger
from os import environ

LOGGER = getLogger(__name__)

try:

    from os import getenv
    import sys
    import os
    from dotenv import load_dotenv
    from base64 import b64decode as who
    from pykillerx.helper import *
    from pykillerx.config import *
    load_dotenv("config.env", override=True)
except:
    print("not installed pykillerx")


API_ID = int(getenv("API_ID", "")) 
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", ""))
BOT_TOKEN = getenv("BOT_TOKEN")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PACK_NAME = getenv("PACK_NAME", "kang pack")
GCAST_BLACKLIST = {int(x) for x in getenv("GCAST_BLACKLIST", "").split()}


DB_URL = getenv("DATABASE_URL")

OPENAI_API = getConfig("OPENAI_API")

# don't kanger repo this !!!
CHANNEL = "@RendyProjects"
SUPPORT = "@pantekyks"

BOT_VER = "0.3.2@dev"
BRANCH = getenv("BRANCH", "DarkWeb") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", None)
STRING_SESSION3 = getenv("STRING_SESSION3", None)
STRING_SESSION4 = getenv("STRING_SESSION4", None)
STRING_SESSION5 = getenv("STRING_SESSION5", None)
STRING_SESSION6 = getenv("STRING_SESSION6", None)
STRING_SESSION7 = getenv("STRING_SESSION7", None)
STRING_SESSION8 = getenv("STRING_SESSION8", None)
STRING_SESSION9 = getenv("STRING_SESSION9", None)
STRING_SESSION10 = getenv("STRING_SESSION10", None)
