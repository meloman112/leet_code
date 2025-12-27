n = int(input('n = '))

total_sum = 0
item = 0
while total_sum < n:
    item += 1
    total_sum += 1/item
print(f'summma = {total_sum - 1/item}')
print(f'k = {item}')