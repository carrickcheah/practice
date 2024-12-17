# Explanation of Logic for maxProfit Function

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit from buying and selling stock.

        Args:
            prices (List[int]): List of stock prices where prices[i] is the price on day i.

        Returns:
            int: The maximum profit possible. Returns 0 if no profit can be made.
        """
        # Initialize variables to track the minimum price and maximum profit
        min_price = float('inf')  # Start with a very high value to ensure any price is smaller
        max_profit = 0  # Start with no profit

        # Iterate through the list of prices
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price

            # Calculate profit for the current price
            profit = price - min_price

            # Update the maximum profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit

        # Return the maximum profit found
        return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(prices))  # Output: 5

# Step-by-Step Explanation:
# 1. Initialize `min_price` as infinity and `max_profit` as 0.
# 2. Iterate over each price in the list:
#    - Check if the current price is lower than `min_price`. If so, update `min_price`.
#    - Calculate the current profit by subtracting `min_price` from the current price.
#    - If the calculated profit is greater than `max_profit`, update `max_profit`.
# 3. Continue until all prices are processed.
# 4. Return `max_profit` as the result.

# Example Walkthrough:
# Prices = [7, 1, 5, 3, 6, 4]
# Day 1: price = 7, min_price = 7, profit = 0, max_profit = 0
# Day 2: price = 1, min_price = 1, profit = 0, max_profit = 0
# Day 3: price = 5, min_price = 1, profit = 4, max_profit = 4
# Day 4: price = 3, min_price = 1, profit = 2, max_profit = 4
# Day 5: price = 6, min_price = 1, profit = 5, max_profit = 5
# Day 6: price = 4, min_price = 1, profit = 3, max_profit = 5
# Final Output: max_profit = 5
