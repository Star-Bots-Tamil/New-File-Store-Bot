import os
from os import getenv, environ
from dotenv import load_dotenv


load_dotenv()
bot_name = "File To Link Bot"
mv_rockers = "https://t.me/Star_Moviess_Tamil"
movie_laab = "https://t.me/Star_Bots_Tamil"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '11973721'))
    API_HASH = str(getenv('API_HASH', '5264bf4663e9159565603522f58d3c18'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '7166851812:AAFU0HZLmdZnfPtRlMFGmb1c9PNeaAzf9hE'))
    name = str(getenv('name', 'file2link_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '7'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001871766752'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1001821439025'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'file-to-link-bot-gx9j.onrender.com')) # starmovies.onrender.com
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "1391556668").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'TG_Karthik'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Star_Bots_Tamil')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @TG_Karthik ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
