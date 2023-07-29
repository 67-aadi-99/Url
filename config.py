# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "14232290"))
API_HASH = os.environ.get("API_HASH", "72f54b0283f40d476b2263a247253e9b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "16375322897:AAGkkWRPbcKohPZB-dvNtjroEOTDJAf5f0o")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "").split("1882381432") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Nokart")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Nokart:aadi@lali@nokart.azzth4g.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1882381432")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "False"
