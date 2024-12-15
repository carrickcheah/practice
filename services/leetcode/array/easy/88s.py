# Solution: Merge Sorted Array

## Step-by-Step Guide

# 1. Identify the Problem
# - We are given two sorted arrays, nums1 and nums2.
# - nums1 has extra space to accommodate elements from nums2.
# - Merge nums2 into nums1 in-place, resulting in a single sorted array.

# 2. Understand the Solution
# - Utilize a two-pointer approach starting from the end of both arrays.
# - Compare elements from the end of nums1 and nums2.
# - Place the larger element in the last position of nums1.

# 3. Define Parameters and Requirements
# - nums1: List[int], has a length of m + n with extra space at the end.
# - nums2: List[int], has a length of n.
# - m: Number of valid elements in nums1.
# - n: Number of valid elements in nums2.

# Constraints:
# - The inputs are sorted in non-decreasing order.
# - Modify nums1 in-place without using extra space.

# 4. Plan Step-by-Step Execution
# - Step 1: Start from the end of nums1 and nums2.
# - Step 2: Compare elements from nums1 and nums2.
# - Step 3: Place the larger element in the current position of nums1.
# - Step 4: Repeat until all elements from nums2 are placed in nums1.

# Flowchart:
# 
#  +---------------------------------------------+
#  | Initialize pointers:                        |
#  | p1 = m - 1, p2 = n - 1, p = m + n - 1      |
#  +---------------------------------------------+
#                 |
#                 v
#  +---------------------------------------------+
#  | While p2 >= 0:                              |
#  |   If p1 >= 0 and nums1[p1] > nums2[p2]:     |
#  |       nums1[p] = nums1[p1]                  |
#  |       Decrement p1                          |
#  |   Else:                                     |
#  |       nums1[p] = nums2[p2]                  |
#  |       Decrement p2                          |
#  |   Decrement p                               |
#  +---------------------------------------------+
#                 |
#                 v
#  +---------------------------------------------+
#  | nums1 is now merged and sorted.             |
#  +---------------------------------------------+

from typing import List

class Solution:
    def merge(self, nums1: List[int],
              m: int, 
              nums2: List[int], 
              n: int
    ) -> None:
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        p1 = m - 1  # Pointer for nums1 (excluding extra space)
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for the last position in nums1

        # Merge nums1 and nums2 from the end
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# Example Usage
solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
