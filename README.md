# WhatsApp Bot by NandhaBots 🚀

A simple, smart WhatsApp bot built with Python using the neonize library. Deploy easily on Termux and connect via QR code.

[![GitHub Repo](https://github.com/NandhaxD/whatsApp_Bot)](https://github.com/NandhaxD/whatsApp_Bot)

## 📱 Quick Start -  Only Two Ways to Step

### 1. Generate Session File (Termux)

`python gen.py`

- Enter phone number ( format : 91xxxx )
- Pair the code with **WhatsApp → Linked Devices → Link With Phone Number Instead**
- Press `Ctrl+\` to exit → **Session file created**

### 2. Run Bot

`python3 -m nandha`

**✅ Your bot is ready!**

## 🛠️ Termux Setup


```
pkg update -y && pkg upgrade -y
pkg install python git ffmpeg -y
pip install -r requirements.txt
```

## 🌿 Environment

Set your environment using ```mv .env.example .env && nano .env```
This is the format
```env
OWNER_UID=9111111111111  # Owner number 
OWNER_GUID=211364584902856  # Owner lid
DB_URL='' # Mongo URI
DB_NAME='whatsappbot' # Database name
MAX_COV_CHATS=10
GROQ_API_KEY='' # Apikey groq
```


## ✨ Features
- ✅ QR-based WhatsApp connection
- ✅ Termux-friendly deployment
- ✅ Simple one-command start
- ✅ Customizable via `config.py`

## ❗ Need Help?
Facing any deployment issues?  
**Contact: [@nandhasupport](https://t.me/nandhasupport)**

---

**Made with ❤️ by [NandhaXD](https://github.com/NandhaxD)**  
⭐ **Star this repo if it helps!**





