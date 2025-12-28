from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        funcs_time = {}
        stack = []
        for log in logs:
            if 'start' in log:
                stack.append(log)
            else:
                func, _, time = log.split(":")
                _, _, start_time = stack.pop()
                funcs_time[func] =

if __name__ == '__main__':
    print(Solution().exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))

