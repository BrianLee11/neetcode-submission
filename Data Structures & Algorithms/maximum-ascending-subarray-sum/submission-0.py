from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        int_max_sum = nums[0]
        int_current_sum = nums[0]
        for index in range(1, len(nums), 1):
            # strictly increasing
            if nums[index] > nums[index - 1]:
                int_current_sum += nums[index]
            else:
                int_current_sum = nums[index]

            if int_max_sum < int_current_sum:
                int_max_sum = int_current_sum

        return int_max_sum
