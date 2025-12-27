from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_x = nums[:n]
        nums_y = nums[n:]
        new_list = []
        for i in range(n):
            new_list.append(nums_x[i])
            new_list.append(nums_y[i])
        return new_list
if __name__ == '__main__':
    print(Solution().shuffle(nums=[2,5,1,3,4,7], n=3))