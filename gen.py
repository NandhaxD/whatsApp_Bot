import sys
import config

from neonize.client import NewClient
from neonize.events import ConnectedEv, PairStatusEv

number = input('Number : ')

client = NewClient(config.session_name)
client.PairPhone(number, show_push_notification=True)

@client.event(PairStatusEv)
def on_paired(_: NewClient, message: PairStatusEv):
      print(f"✓ Logged in as: {message.ID.User}")
      sys.exit(0)
