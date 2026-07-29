from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        int_n = len(nums)
        int_threshold = int_n // 2
        dictionary_nums = defaultdict(int)

        for number in nums:
            dictionary_nums[number] += 1

            if (int_threshold < dictionary_nums[number]):
                return number
                