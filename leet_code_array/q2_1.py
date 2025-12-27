from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicated_int = sum(nums) - sum(set(nums))
        n = len(nums)
        expected_int = (n * (n + 1) / 2) - (sum(nums) - duplicated_int)
        return [duplicated_int, int(expected_int)]
if __name__ == '__main__':
    print(Solution().findErrorNums(nums=[2,2]))
