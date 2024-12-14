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
        min_price = float('inf')  # Start with a very high value
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
