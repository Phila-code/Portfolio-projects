stock_prices = {
    "AAPL": 175,
    "GOOGL": 2825,
    "MSFT": 299,
    "TSLA": 709,
    "AMZN": 3342
}

def get_user_portfolio():
    portfolio = {}
    print("Enter your stock holdings. Type 'done' to finish")

    while True:
        stock = input("Enter stock:").upper()
        if stock == "Done":
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}:"))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:  
            print("Please enter a valid number.")

    return portfolio

def calculate_investment(portfolio):
    total_value = 0
    print("\n Portfolio Summary:") 
    for stock, qty in portfolio.items():
        price = stock_prices[stock] 
        value = price * qty
        total_value += value
        print(f"{stock}:{qty} shares ${price} = ${value}")
    print(f"\n Total Investment Value: ${total_value}")
    return total_value

def save_to_file(portfolio, total, filename="portfolio_summary.txt"):
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"\n Total Investment: ${total}")
    print(f"Portfolio saved to {filename}") 
portfolio = get_user_portfolio()
port = calculate_investment(portfolio)


