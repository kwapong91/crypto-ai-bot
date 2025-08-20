from broker_adapter.exchange import BrokerAdapter

broker = BrokerAdapter()

live_broker = BrokerAdapter(mode=False)
paper_broker = BrokerAdapter(mode=True)

print(paper_broker.place_order("BTC/USD", "buy", 1.0, price=400))
# print(live_broker.get_price('BTC/USD'))

