import os
from dotenv import load_dotenv

load_dotenv("./.env")

#URLs
INSTAGRAM_LOGIN_PAGE_URL = os.getenv("INSTAGRAM_LOGIN_PAGE_URL")
GOOGLE_PLAY_URL = os.getenv("GOOGLE_PLAY_URL")

#Credentials
WRONG_PASSWORD = os.getenv("WRONG_PASSWORD")
WRONG_LOGIN = os.getenv("WRONG_LOGIN")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_LOGIN = os.getenv("MY_LOGIN")
