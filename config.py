import os

API_ID = API_ID = 3748059

API_HASH = os.environ.get("API_HASH", "f8c9df448f3ba20a900bc2ffc8dae9d5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6543084771:AAEeKisThX6Y1yjAupy4Kb2eX1zyU7G_fyY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1993514215))

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1993514215").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins List Does Not Contain Valid Integers.")
ADMINS.append(OWNER)


