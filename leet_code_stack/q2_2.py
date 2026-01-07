from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp_s = stack.pop()
                result[temp_s] = i - temp_s
            stack.append(i)
        return result

if __name__ == '__main__':
    print(Solution().dailyTemperatures(temperatures = [73,74,75,71,90,72,76,73]))

