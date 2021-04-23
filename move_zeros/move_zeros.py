class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        is_reversed = True
        num_len = len(nums)
        while(is_reversed):
            is_reversed = False
            for i in range(num_len - 1):
                first = nums[i]
                second = nums[i + 1]
                if ((first==0 and not(first==0 and second==0))):
                    nums[i] = second
                    nums[i + 1] = first
                    is_reversed = True
        return nums
            