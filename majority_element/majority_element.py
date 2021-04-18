class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_number_of_num = 0
        max_num = 0
        for num in set(nums):
            number_of_num = nums.count(num)
            if number_of_num > max_number_of_num:
                max_num = num
                max_number_of_num = number_of_num
        return max_num