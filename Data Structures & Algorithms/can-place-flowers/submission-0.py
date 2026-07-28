from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if (n == 0):
            return True

        count = 0       

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                count += 1
                return n <= 1
            elif flowerbed[0] == 1:
                return n == 0

        if (flowerbed[0] == 0) and (flowerbed[1] == 0):
            flowerbed[0] = 1
            count += 1

        for index in range(1, len(flowerbed) - 1, 1):
            if flowerbed[index] == 0:
                if (flowerbed[index - 1] == 0) and (flowerbed[index + 1] == 0):
                    flowerbed[index] = 1
                    count += 1

        if (flowerbed[-1] == 0) and (flowerbed[-2] == 0):
            flowerbed[-1] = 1
            count += 1
        
        return n <= count