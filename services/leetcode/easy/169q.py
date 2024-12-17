from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        pass






"""

169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 
Example 1:
Input: nums = [3,2,3]
Output: 3


Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?

"""

# Step 1: Understand the Problem
# You are given an array of numbers (like [3, 2, 3]), where each number represents a "candy color." 
# Your job is to figure out which number (candy color) appears more than half the time in the array.

# Step 2: Define What Needs to Happen
# Count how many times each number appears in the array.
# Identify the number that appears more than half of the array's length (i.e., n / 2).
# Return that number as the "majority element."

# Step 3: Plan How to Solve the Problem
# Option 1: Use a dictionary to keep track of how many times each number appears:

# Loop through the array.
# For each number, increase its count in the dictionary.
# Check if any number's count is greater than n / 2.
# Option 2: Use a "vote" method (Boyer-Moore Voting Algorithm):

# Keep a candidate for the majority element and a count.
# As you loop through the array, adjust the count based on whether the current number matches 
# the candidate.
# At the end, the candidate will be the majority element.


# Step 4: Determine the Result
# After following your plan, you’ll get the number that appears more than half the time. For example:

# If nums = [3, 2, 3], the result is 3 because it appears 2 times, which is more than half of 3.
# If nums = [2, 2, 1, 1, 1, 2, 2], the result is 2 because it appears 4 times, 
# which is more than half of 7.


# Step 5: Test Your Solution
# Test your solution with various inputs:

# nums = [3, 2, 3] → Expected: 3
# nums = [2, 2, 1, 1, 1, 2, 2] → Expected: 2
# nums = [1, 1, 1, 2, 2] → Expected: 1


# Step 6: Think About Edge Cases
# What if the array has only one number? (nums = [1]) → Majority element is 1.
# What if all numbers are the same? (nums = [2, 2, 2, 2]) → Majority element is 2.
# What if the array is very large? Optimize your solution to work efficiently, 
# such as using the Boyer-Moore algorithm for O(n) time and O(1) space.

