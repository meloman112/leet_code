from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        len_max = 0
        local_max = 0
        for item in nums:
            if item:
                local_max += 1
            else:
                len_max = local_max if local_max > len_max else len_max
                local_max = 0
        else:
            len_max = local_max if local_max > len_max else len_max
        return len_max
if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes(nums=[1,1,0,1,1,1]))
