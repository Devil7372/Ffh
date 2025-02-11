import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "21185801"))
API_HASH = os.environ.get("API_HASH", "4235ef431f138309cb9f56ae179a24ba")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7855422315:AAGUELg7hjkZKQKL4lr_rUVPqWLh91MG5dE")
ADMIN = int(os.environ.get("ADMIN", "7057341064"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/f6.jpg")
