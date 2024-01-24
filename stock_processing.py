def getDataPoint(stock_name, bid_price, ask_price):
    """
    Returns a tuple of stock name, bid price, ask price, and calculated price (average of bid and ask).
    """
    price = (bid_price + ask_price) / 2
    return stock_name, bid_price, ask_price, price

def getRatio(stock_price_A, stock_price_B):
    """
    Returns the ratio of the two stock prices.
    """
    if stock_price_B == 0:
        raise ValueError("Cannot divide by zero. Stock B price should be greater than zero.")
    return stock_price_A / stock_price_B

def main():
    """
    Outputs correct stock info, prices, and ratio.
    """
    # Example data for stock A and stock B
    stock_A_name = "Stock A"
    stock_A_bid_price = 100
    stock_A_ask_price = 105

    stock_B_name = "Stock B"
    stock_B_bid_price = 80
    stock_B_ask_price = 85

    # Get data points for both stocks
    stock_A_data = getDataPoint(stock_A_name, stock_A_bid_price, stock_A_ask_price)
    stock_B_data = getDataPoint(stock_B_name, stock_B_bid_price, stock_B_ask_price)

    # Display stock info, prices, and ratio
    print(f"Stock A Info: {stock_A_data}")
    print(f"Stock B Info: {stock_B_data}")

    # Calculate and display the ratio of the two stock prices
    ratio = getRatio(stock_A_data[3], stock_B_data[3])
    print(f"Ratio of Stock A to Stock B prices: {ratio}")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
