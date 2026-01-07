from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [heights]
        for l in ff(heights, 2):
            print(l)
        while stack:
            temp_list = stack.pop()
            min_el = min(temp_list)
            list_len = len(temp_list)
            area = min_el * list_len
            max_area = area if max_area < area else max_area
            min_count = temp_list.count(min_el)





            if list_len > 1:
                min_el_indx = temp_list.index(min_el)
                if temp_list[:min_el_indx]:
                    stack.append(temp_list[:min_el_indx])
                if temp_list[min_el_indx+1:]:
                    stack.append(temp_list[min_el_indx+1:])

            # print(stack)
            # print(max_area)
        return max_area

def ff(ls, m):
    st_sp = 0
    for ind, el in enumerate(ls):
        if el == m:
            yield ls[st_sp:ind]
            st_sp = el-1


if __name__ == '__main__':
    print(Solution.largestRectangleArea(Solution(), heights=[4,3,5,30,9,2,8,4,1,2,3,8,3,5,4,7,9]))