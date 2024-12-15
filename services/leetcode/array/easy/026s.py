class Solution:
    def removeElement(self, 
                      nums: List[int], 
                      val: int
    ) -> int:

        if not nums:
            return 0

        pointer = 0
  
        for i in range(len(nums)):
            if val != nums[i]:  
                nums[pointer] = nums[i]  
                pointer += 1      

        return pointer

val = 3
nums = [3,2,2,3]
solution = Solution()
print(solution.removeElement(nums,val))
