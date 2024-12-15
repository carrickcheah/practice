class Solution:
    def removeDuplicates(self, 
                         nums: List[int]
                         
    ) -> int:

        """
        26. Remove Duplicates from Sorted Array
        Check nums[i] by loops.

        Args:
        nums: List[int] : input array of integers
     
        return: 
            int : number of unique elements in the array

        """


        # check the list is it empty
        if not nums:
            return 0
        


