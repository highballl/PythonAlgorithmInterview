from functools import reduce
from collections import Counter
nums = [1,2,3,4]
#nums = [1, 2, 3, 5, 2, 4, 7, 4]
result = []

temp = Counter(nums)

for num in nums:
    mul = 1
    for k, v in temp.items():
        if num == k:
            mul *= reduce(lambda x, y: x**y, [k, v-1])
        else:
            mul *= reduce(lambda x, y: x**y, [k, v])
    result.append(mul)

print(result)