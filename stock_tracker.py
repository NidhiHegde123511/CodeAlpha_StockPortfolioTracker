
# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}

print("📊 Stock Portfolio Tracker")
print("Available stocks: ", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("⚠️ Stock not found in our database.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("❌ Quantity must be positive.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n🧾 Portfolio Summary:")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_value}")

# (Optional) Save to file with UTF-8 encoding
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
        file.write("📊 Stock Portfolio Summary\n")
        file.write("------------------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock}: {qty} × ₹{price} = ₹{value}\n")
        file.write(f"\n💰 Total Investment Value: ₹{total_value}\n")
    print("✅ Summary saved to 'portfolio_summary.txt'.")
