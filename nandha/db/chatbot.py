
from nandha import database 

import config


col = database['chat_bot']

def add_chat(chat_id: int) -> bool:
    
    if chat_id not in config.chatbot_chats:
        config.chatbot_chats.append(chat_id)
    data = {
        '$set': {
            'chat_id': chat_id
        }
    }
    result = col.update_one({'chat_id': chat_id}, data, upsert=True)
    return bool(result.acknowledged)

def remove_chat(chat_id: int) -> bool:

    if chat_id in config.chatbot_chats:
        config.chatbot_chats.remove(chat_id)
        
    chat = {'chat_id': chat_id}
    data = col.delete_one(chat)
    return bool(data.deleted_count)

def get_all_chat() -> list[int]:
    chats = col.find({}, {'chat_id': 1})
    return [chat['chat_id'] for chat in chats] if chats else []


def get_chat(chat_id: int) -> dict:
    data = col.find_one({'chat_id': chat_id})
    return data if data else {}


def is_chat(chat_id: int) -> bool:
    return bool(col.find_one({'chat_id': chat_id}))
