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


