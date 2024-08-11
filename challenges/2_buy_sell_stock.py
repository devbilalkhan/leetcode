def maxProfit(prices):
    """
    Function to calculate the maximum profit from buying and selling a stock.
    
    :param prices: List of stock prices where prices[i] is the price of the stock on the ith day.
    :return: Maximum profit that can be achieved from a single buy and sell transaction.
    """
    
    # If there are less than 2 prices, no transaction can be made
    if len(prices) < 2:
        return 0
    
    # Initialize pointers for the left (buy) and right (sell) days
    left = 0
    right = 1
    
    # Initialize the maximum profit to 0
    max_profit = 0

    # Iterate through the list of prices
    while right < len(prices):
        # If the price at the left pointer is greater than the price at the right pointer,
        # move the left pointer to the right pointer's position
        if prices[left] > prices[right]:
            left = right
        else:
            # Calculate the current profit
            current_profit = prices[right] - prices[left]
            # Update the maximum profit if the current profit is greater
            max_profit = max(current_profit, max_profit)
        
        # Move the right pointer to the next day
        right += 1
        
    return max_profit
        