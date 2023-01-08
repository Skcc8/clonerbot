from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "22977869")) 
API_HASH = getenv("API_HASH", "9d8d4686d750b29a6cd2b7c73eb16f26")
ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("5759520737:AAGxcApe9YYzj8mAtKjQL57NFaReJPm91_c")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("-1001700056767"))
MONGO_DB_URI = getenv("mongodb+srv://musicbot:musicbot@cluster0.i889qsr.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5899030234").split()))
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG","https://te.legra.ph/file/7fd1cecadabad0bf96733.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/QUEEN_II_SUPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DP_Store_SK_X_Y")
STRING_SESSION = getenv("STRING_SESSION", "BQAhGFBjNsa04gEFDVkffphIEwFx9dYvBY5QZ_4uyA2vsVAK1i3-5z8w3RF7y_rQkrjpAAOlgGRIMaugDtIOlHv0Y7gzqzvU7_kctpjKIpMJybbE1fyXCBWAbLuBPY5gkR3ZJjU7QOhbjxHTgFaVi4Y_CucpptM_HqmmmK0WSez6MKzUQQcg0vCKDUHuzBn9eH61oC25_oAVl882Xe9zXRHyaf43WT-C5tw89EzrH7eiDyH0zIXtc-eZ1eUivT1eTYRljMHk_3kIfEE2yLuBDvePuN1SrgpB6NvdsOMFPDSavdxOwbVuAmWDM6kAeN6yXvWN7w3F5WCyqlFwaZStiD0VAAAAAWBSOSEA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5683603896").split()))
