from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = prices.copy()
        for i in range(len(prices)):
            temp_stack = []
            while stack:
                item = stack.pop()
                if prices[item] < prices[i]:
                    temp_stack.append(item)
                else:
                    result[item] -= prices[i]
            temp_stack.append(i)
            stack = temp_stack
        return result


if __name__ == '__main__':
    print(Solution().finalPrices(prices=[8,4,6,2,3]))

"""
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []                 # стек индексов
        result = prices.copy()     # сразу кладём исходные цены

        for i in range(len(prices)):
            # пока текущая цена даёт скидку тем, кто ждёт
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] -= prices[i]

            # текущий элемент сам ждёт скидку
            stack.append(i)

        return result

"""