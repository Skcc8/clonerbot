from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "22839633")) 
API_HASH = getenv("API_HASH", "5287f94935d4830bbbb242fc09ef050d")
ASS_HANDLER = list(getenv("ASS_HANDLER", "/").split())
BOT_TOKEN = getenv("5857733358:AAFY6XAPx1RgICtV8QJVJPClgY9HN6G0CPE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("-1001700056767"))
MONGO_DB_URI = getenv("mongodb+srv://musicbot:musicbot@cluster0.i889qsr.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5899030234").split()))
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG","https://te.legra.ph/file/7fd1cecadabad0bf96733.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/QUEEN_II_SUPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/queenmusicupdates")
STRING_SESSION = getenv("STRING_SESSION", "BQCtkmzDiaGFY9kSty5cqayvYh5jioU7fvIZxXMj9gdIbji7Q3EuKdrceZEOlwE0aGvsfSOo6Kr2XTdotXweOc1Ij_Zifm_rS9W8RYt2lHOgB1SvYR5Hsyfxj-eBI35RWVBqoBUYrLItzEteV_oR1SOr3kI3GfPTRO_f_V_2mc2d_4ke3FtkgkxZ0GSo6PhsxBXOpTOqjhvZ7clJT1Ke249NLGbKoQl3kihhJHMWheWFI-HtowDkjzCu2G-xZOPpZkDRxPjJPJIOJI-BzU0CULpepeDEjHbRki2Zd6-oPhhwvLNo_KKmqLq_Et5V4B9_g2vCojmtnqnexnqfHy814U9bAAAAATSXpf0A")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5575020219").split()))
