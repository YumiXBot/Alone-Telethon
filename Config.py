import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6127476417:AAFwCcnDziasXrdRCad7dyhaZz2joA6Kd-o")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJQBu2Ig6ankQ_EZBGl-7IkV8svybov4S8QV16FHkmR9JxHUTRhFltIdz7qWREV9ox3rzFDd33fqkcZJp5e82PF1t8LYShVd30tqBFYm5VL2LvRH-h9ugp1lXPvRfPmcPDiP6vpIZwGnixOpguhogQZrisdOe0zlBJs4qfFQos7FNC8XJXgOeD8WRU9owkEBM2Pqs68YBx3zdR4fuMMRlrVVdLh3TvObQPL1e29ja1Shn4LCQgqWv5XIGt1CkGZFvic4hXykbQVDctQrHBXPTFZYpXW_uAkPuLllBasOFY8Wta4Qd5NS_lkMmxFlG7rNMWiNezbQTDbT49E5EU8OHy0UEs4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "AlonePvtBot")
    SUPPORT = os.environ.get("SUPPORT", "AlonesHeaven") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "AloneXBots") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/f857bd830b793c86019ab.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5693644992")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "5400")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True".get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
