from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in the array using a dictionary-based counting approach.

        Args:
            nums (List[int]): The input array of numbers.

        Returns:
            int: The majority element.
        """

        counts = {}

        for i in nums:
            counts[i] = counts.get(i, 0) + 1  # Increment the count for the current number

            if counts[i] > len(nums) // 2:
                return i  # Return the majority element when found

# Example usage for majorityElement:
nums = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
print(solution.majorityElement(nums))  # Output: 2





