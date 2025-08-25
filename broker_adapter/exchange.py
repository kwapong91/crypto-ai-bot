# Need to build classes for each


# main class

class BrokerAdapter:
    def __init__(self, mode=True):
        self.mode = mode
        if not self.mode:
            import ccxt
            self.exchange = ccxt.coinbase()
        print("BrokerAdapter created!")

    def get_balance(self):
        account_balance = {'USD': 1000}
        return account_balance
    
    def get_price(self, crypto):
        if self.mode == True:
            price = {
                'symbol': crypto,
                    'price': 1000
                    }
            return price
        else:
            ticker = self.exchange.fetch_ticker(crypto)
            ticker_data = {
                'symbol': crypto,        # which market
                'timestamp': ticker["timestamp"], # raw time in ms
                'datetime': ticker["datetime"], # human-readable time
                'bid': ticker["bid"],           # current highest buy offer
                'ask': ticker["ask"],           # current lowest sell offer
                'last': ticker["last"],          # last traded price
                'close': ticker["last"],         # closing price for this period
                'info': {                   # raw exchange info if needed for debugging
                    'trade_id': ticker['info']['trade_id'],
                    'product_id': ticker['info']['product_id'],
                    'price': ticker['info']['price'],
                    'size': ticker['info']['size'],
                    'time': ticker['info']['time'],
                    'side': ticker['info']['side'],
                    'exchange': ticker['info']['exchange']
                }
            }
        return ticker_data

    def place_order(self, symbol, order_type, side, amount, price=None):
        # Needs to place a buy or sell order
        import uuid

        if order_type == "Market":
            status = "Filled"
        elif order_type == "Limit":
            status = "Open"
        else:
            status = "Unknown"

        order = {
                "id": uuid.uuid4().hex[:8],
                "symbol": symbol,
                "type": order_type,
                "side": side,
                "amount": amount,
                "price": price,
                "status": status
                }
        
        return order

    def cancel_order(self, order_id):
        canceled_order = {
                "id": order_id,
                "status": "Canceled"
                }
        return canceled_order

    # def get_position(self):
    #     # Position that is being held
           