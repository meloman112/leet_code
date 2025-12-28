from typing import List


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = ["+", "-", "*", "/"]
        def calculate(operand, first_el, second_el):
            first_el, second_el = int(first_el), int(second_el)
            if operand == "+":
                return first_el + second_el
            elif operand == "-":
                return  first_el - second_el
            elif operand == "/":
                return int(first_el / second_el)
            else:
                return first_el * second_el

        stack = []
        for t in tokens:
            if t in operands:
                b = stack.pop()
                a = stack.pop()

                stack.append(calculate(t, a, b))
            else:
                stack.append(int(t))

        return stack[0]


if __name__ == '__main__':
    print(Solution().evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


'''class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop()+stack.pop())
            elif ch == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif ch == '*':
                stack.append(stack.pop()*stack.pop())
            elif ch == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(ch))
        return stack[0]
        '''