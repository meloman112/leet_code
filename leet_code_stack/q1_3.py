from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        funcs_time = {str(i): 0 for i in range(n)}
        stack = []
        for log in logs:
            if 'start' in log:
                stack.append(log)
            else:
                func, _, end_time = log.split(':')
                _, _, start_time = stack.pop().split(':')
                delta = int(end_time) - int(start_time) + 1
                funcs_time[func] += delta
                if len(stack) != 0:
                    old_func, _, _ = stack[-1].split(":")
                    funcs_time[old_func] -= delta
        return list(funcs_time.values())

if __name__ == '__main__':
    print(Solution().exclusiveTime(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))

