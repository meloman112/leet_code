from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_list = sorted(nums)
        new_list = []
        for el in nums:
            new_list.append(sort_list.index(el))
        return new_list

if __name__ == '__main__':
    print(Solution().smallerNumbersThanCurrent(nums=[8,1,2,2,3]))
