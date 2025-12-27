from typing import List


class Solution:
    def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums)+1)) - set(nums))

if __name__ == '__main__':
    print(Solution().findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1]))
