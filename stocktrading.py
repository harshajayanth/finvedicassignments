class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class StockTradingSimulator:
    def __init__(self):
        self.balance = 10000 

    def buy_stock(self, stock, shares):
        total_cost = stock.price * shares
        if total_cost > self.balance:
            print("Insufficient balance to buy", shares, "shares of", stock.symbol)
            return
        
        self.balance -= total_cost
        print(f"Bought {shares} shares of {stock.symbol} at ${stock.price:.2f} each. Total cost: ${total_cost:.2f}.")
        print(f"Current Balance: ${self.balance:.2f}")

    def sell_stock(self, stock, shares):
        total_sale = stock.price * shares
        self.balance += total_sale
        print(f"Sold {shares} shares of {stock.symbol} at ${stock.price:.2f} each. Total sale: ${total_sale:.2f}.")
        print(f"Current Balance: ${self.balance:.2f}")


if __name__ == "__main__":
    simulator = StockTradingSimulator()

    # Creating a stock
    apple_stock = Stock("AAPL", 150)

    # Buying stocks
    simulator.buy_stock(apple_stock, 10) 

    # Selling stocks
    simulator.sell_stock(apple_stock, 5)  
