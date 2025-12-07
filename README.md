# WhatsApp Bot by NandhaXD 🚀

A simple, smart WhatsApp bot built with Python using the neonize library. Deploy easily on Termux and connect via QR code.

[![GitHub Repo](https://github.com/NandhaxD/whatsApp_Bot)](https://github.com/NandhaxD/whatsApp_Bot)

## 📱 Quick Start - 4 Simple Steps

### 1. Generate Session File (Termux)

`python gen.py`

- Enter session name (or press Enter for default)
- Scan QR code with **WhatsApp → Linked Devices**
- Press `Ctrl+\` to exit → **Session file created**

### 2. Save Session File

`mv session_name ~/storage/shared/`


### 3. Upload & Configure
- Upload `session_name` file to your GitHub repo
- Edit `config.py` → set `session_name = "your_session_filename"`

### 4. Run Bot

`python3 -m nandha`

**✅ Your bot is ready!**

## 🛠️ Termux Setup


```
pkg update && pkg upgrade
pkg install python git
pip install -r requirements.txt
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




