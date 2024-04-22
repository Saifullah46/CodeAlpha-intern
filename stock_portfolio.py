class Stock:
    def __init__(self, symbol, quantity, purchase_price):
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price

    def current_value(self, current_price):
        return self.quantity * current_price

    def profit_loss(self, current_price):
        return (current_price - self.purchase_price) * self.quantity

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
                return True
        return False

    def total_value(self, stock_prices):
        total = 0
        for stock in self.stocks:
            if stock.symbol in stock_prices:
                total += stock.current_value(stock_prices[stock.symbol])
        return total

    def total_profit_loss(self, stock_prices):
        total = 0
        for stock in self.stocks:
            if stock.symbol in stock_prices:
                total += stock.profit_loss(stock_prices[stock.symbol])
        return total

    def display_portfolio(self, stock_prices):
        print("Stock Portfolio:")
        print("Symbol\tQuantity\tPurchase Price\tCurrent Price\tCurrent Value\tProfit/Loss")
        for stock in self.stocks:
            if stock.symbol in stock_prices:
                current_price = stock_prices[stock.symbol]
                current_value = stock.current_value(current_price)
                profit_loss = stock.profit_loss(current_price)
                print(f"{stock.symbol}\t{stock.quantity}\t\t{stock.purchase_price}\t\t{current_price}\t\t{current_value}\t\t{profit_loss}")
        print(f"\nTotal Portfolio Value: {self.total_value(stock_prices)}")
        print(f"Total Profit/Loss: {self.total_profit_loss(stock_prices)}")

def main():
    portfolio = Portfolio()

    while True:
        print("\n1. Add stock")
        print("2. Remove stock")
        print("3. Display portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price per share: "))
            stock = Stock(symbol, quantity, purchase_price)
            portfolio.add_stock(stock)
            print("Stock added to portfolio.")

        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            if portfolio.remove_stock(symbol):
                print("Stock removed from portfolio.")
            else:
                print("Stock not found in portfolio.")

        elif choice == "3":
            # For simplicity, let's assume we have current prices for each stock
            stock_prices = {
                "AAPL": 150.50,
                "GOOGL": 2700.30,
                "TSLA": 800.25,
                # Add more stocks and their prices as needed
            }
            portfolio.display_portfolio(stock_prices)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
