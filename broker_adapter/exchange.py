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
    
    def get_price(self, symbol):
        if self.mode == True:
            price = {
                'symbol': symbol,
                    'price': 1000
                    }
            return price
        else:
            ticker = self.exchange.fetch_ticker(symbol)
            return {
                'symbol': symbol,
                'price': int(ticker['last'])
                }

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

    # def cancel_order(self):
    #     # Needs to cancel order with order id

    # def get_position(self):
    #     # Position that is being held
           