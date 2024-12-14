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
        counts = {}  # Create a dictionary to store number counts

        for num in nums:  # Loop through each number in the list
            counts[num] = counts.get(num, 0) + 1  
            # Step-by-step:
            # counts[2] = counts.get(2, 0) + 1  | {2: 1}
            # counts[2] = counts.get(2, 1) + 1  | {2: 2}
            # counts[1] = counts.get(1, 0) + 1  | {2: 2, 1: 1}
            # counts[1] = counts.get(1, 1) + 1  | {2: 2, 1: 2}               
            # counts[1] = counts.get(1, 2) + 1  | {2: 2, 1: 3}
            # counts[2] = counts.get(2, 2) + 1  | {2: 3, 1: 3}          
            # counts[2] = counts.get(2, 3) + 1  | {2: 4, 1: 3}

            if counts[num] > len(nums) // 2:  # 10 // 2  # Output: 5
                return num

# Example usage for majorityElement:
nums = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
print(solution.majorityElement(nums))  # Output: 2

"""
Lesson learned:
1. Init Dict 是用{}； assign list 是用[]
2. counts.get(num, 0) , used to get the value of the dict, if the key does not exist, return 0
3. counts[num] , is assign to the dict, if the key does not exist, create a new key-value pair
4. class must be defined before using it
"""