from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        print(nums)

if __name__ == '__main__':
    print(Solution().getConcatenation(nums=[1,2,1]))