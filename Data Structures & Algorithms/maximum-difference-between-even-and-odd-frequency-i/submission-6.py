from collections import defaultdict

class Solution:
    def maxDifference(self, s: str) -> int:
        dictionary_char = defaultdict(int)

        for character in s:
            dictionary_char[character] += 1        

        max_frequency_odd = max(value for value in dictionary_char.values() if value % 2 == 1)
        min_frequency_even = min(value for value in dictionary_char.values() if value % 2 == 0)
        
        return max_frequency_odd - min_frequency_even