from dotenv import load_dotenv ,find_dotenv
import os

env_path = find_dotenv()
load_dotenv(env_path)

support_chat = 't.me/NandhaSupport'
updates_channel = 't.me/NandhaBots'
owner_url = 'https://github.com/nandhaxd'
devs_list = [owner_uid, 
#other
]  

owner_uid = int(os.getenv('OWNER_UID', 9111111111111)) 
owner_guid = int(os.getenv('OWNER_GUID', 211364584902856)) # nandha.utils.get_guid(event)

db_url: str = os.getenv('DB_URL', '') # mongo db uri
db_name = os.getenv('DB_NAME', 'whatsappbot')
session_name = db_name

chatbot_chats: list[int] = []  
max_cov_chats: int = int(os.getenv('MAX_COV_CHATS', 10))

AI_SYS_TXT = '''
Your name is Nandha AI,
You are a programming guy and a mathematician,
You like helping people's,

You clearly explain concepts,
Uses emoji to excite the concepts.

Use only those markdown style formats for response:
*bold*, `word`, ```code```, _italic_, ~Strikethrough~
'''

groq_api_key = os.getenv('GROQ_API_KEY', '') # your groq api-key

MODULE = {};HANDLER = {};ALL_FUNC = set();DISABLED_FUNC = {}

