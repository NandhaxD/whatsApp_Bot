from neonize.client import NewClient
from neonize.utils import build_jid
from pymongo import MongoClient
import config
import logging
import time
import config

fh = logging.FileHandler('logs.txt')
fh.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s - %(message)s")
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logging.basicConfig(level=logging.DEBUG, handlers=[fh, sh])

log = logging.getLogger(__name__)

mdb = MongoClient(config.db_url)
log.info('✅ Successfully connected to MongoDB.')
database = mdb[config.db_name]

self = build_jid(str(config.owner_uid))
client = NewClient(config.session_name)


