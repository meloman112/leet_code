from typing import List


class Solution:
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        push = "Push"
        pop = "Pop"
        max_item = max(target)
        temp_list = []
        length = max_item + 1 if max_item < n else n + 1
        for i in range(1, length):
            temp_list.append(push)
            if i not in target:
                temp_list.append(pop)
        return temp_list


if __name__ == '__main__':
    print(Solution().buildArray(target = [1,4], n = 4))
