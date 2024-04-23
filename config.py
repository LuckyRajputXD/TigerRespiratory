import os

API_ID = API_ID = 20963688

API_HASH = os.environ.get("API_HASH", "964a26dc404aa5e12dfe82ea94ae7ae3
")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7064782752:AAGvY_v7N5StrToJc6l15bJPKAZNy0gIguo")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER",6867189163 ))

LOG = -4189963691

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6867189163").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


