stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "AMZN": 140,   # Amazon
    "MSFT": 320,   # Microsoft
    "GOOGL": 130   # Google
}

portfolio = {}

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter the stocks you own. Type 'done' when finished.\n")

# User input loop
while True:
    stock_name = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    elif stock_name not in stock_prices:
        print("❌ Invalid stock symbol. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("⚠️ Please enter a valid number for quantity.")

# Calculate total investment
total_value = 0
print("\n💼 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save_option = input("\nWould you like to save this report? (yes/no): ").lower()
if save_option == "yes":
    file_name = "portfolio_report.txt"
    with open(file_name, "w") as file:
        file.write("📊 STOCK PORTFOLIO REPORT\n")
        file.write("--------------------------\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment: ${total_value}\n")
    print(f"✅ Report saved successfully as '{file_name}'")

print("\nThank you for using the Stock Portfolio Tracker! 🚀")
