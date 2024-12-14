from typing import List

class Solution:
    def removeElement(self, 
                      nums: List[int],
                      val: int) -> int:

        

        """
        Remove all occurrences of 'val' in-place and return the new length (k).

        Args:
        nums (List[int]): The input array.
        val (int): The value to remove.

        Returns:
        int: The number of elements not equal to val.
        """




















# class Solution:
#     def removeElement(self, nums, val):
#         """
#         Remove all occurrences of 'val' in-place and return the new length (k).

#         Args:
#         nums (List[int]): The input array.
#         val (int): The value to remove.

#         Returns:
#         int: The number of elements not equal to val.
#         """
#         k = 0  # Pointer for the next position of the element not equal to val

#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]  # Move valid element to the front
#                 k += 1

#         return k

# # Example Usage:
# nums1 = [3, 2, 2, 3]
# val1 = 3
# solution = Solution()
# k1 = solution.removeElement(nums1, val1)
# print("Output:", k1, ", nums:", nums1[:k1])

# nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
# val2 = 2
# k2 = solution.removeElement(nums2, val2)
# print("Output:", k2, ", nums:", nums2[:k2])
