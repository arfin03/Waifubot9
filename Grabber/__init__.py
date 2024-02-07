import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = 5932230962
sudo_users = ["5932230962", "5932230962"]
GROUP_ID = -1001924285977
TOKEN = "6512496443:AAFKX49iM1N6Go0wYDACLOvae33TNK_hqss"
mongo_url = "mongodb+srv://husbando:husbando@cluster0.pipkivx.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph/file/72ea883532b722f405059.jpg", "https://telegra.ph/file/72ea883532b722f405059.jpg"]
SUPPORT_CHAT = "TEAMS_VG"
UPDATE_CHAT = "TEAMS_VG"
BOT_USERNAME = "Husbando_x_robot"
CHARA_CHANNEL_ID = -1001924285977
api_id = 20574660
api_hash = "6e21188e487b96af1ff5429dedada8ff"


application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']



