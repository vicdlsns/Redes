from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os
pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-12efc6a7-dbc9-44cd-91df-d4977f237ed8'
pnconfig.subscribe_key = 'sub-c-724ad54c-da65-11e9-a6c8-3e57a349bb32'
pnconfig.ssl = True
pubnub = PubNub(pnconfig)
def my_publish_callback(envelope, status):
  # Check whether request successfully completed or not
  if not status.is_error():
    pass
class MySubscribeCallback(SubscribeCallback):
  def presence(self, pubnub, presence):
    pass
  def status(self, pubnub, status):
    pass
  def message(self, pubnub, message):
    print ("from device 2: " + message.message)
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()
## publish a message
while True:
  msg = input("Input a message to publish: ")
  if msg == 'exit': os._exit(1)
  pubnub.publish().channel("chan-1").message(str(msg)).pn_async(my_publish_callback)