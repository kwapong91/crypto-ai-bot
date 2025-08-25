<<<<<<< HEAD
from broker_adapter.exchange import BrokerAdapter
import time
from coin_mapping import alias_map
live_broker = BrokerAdapter(mode=False)

def user_crypto_choose():
    while True:
        user_crypto = input("What cryptocurrency would you like to get the price for?")
        if user_crypto in alias_map:
            crypto_choose = alias_map[user_crypto]
            return crypto_choose
        else:
            print("Invalid cryptocurrency. Please try again.")
    
crypto_choose = user_crypto_choose()

for i in range(10):
    live_price = live_broker.get_price(crypto_choose)
    price = live_price['info']['price']
    print(price)
    time.sleep(5)

# What I need to do next is print this log out: 2025-08-24 12:00:00 | BTC/USD | 113,000.00 | HOLD
=======
from broker_adapter.exchange import BrokerAdapter
import time

live_broker = BrokerAdapter(mode=False)

for i in range(10):
    live_price = live_broker.get_price("BTC/USD")
    price = live_price['price']
    if price <= 50000:
        print('Buy')
    elif price >= 60000:
        print('Sell')
    time.sleep(5)


>>>>>>> 9b6785c26cda38f352000d95009c9279a894c77a
