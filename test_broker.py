from broker_adapter.exchange import BrokerAdapter

broker = BrokerAdapter()

live_broker = BrokerAdapter(mode=False)
paper_broker = BrokerAdapter(mode=True)


# print(live_broker.get_price('BTC/USD'))
order_id = paper_broker.place_order("USD", 'Market', 'Sell', 1.100, price=None)['id']
print(paper_broker.cancel_order(order_id))
