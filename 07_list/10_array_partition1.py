#nums = [1,4,3,2]
# output = 4
nums = [6,2,6,5,1,2]
# output = 9

nums.sort()
result = 0
for i in range(len(nums)):
    if i % 2 == 0:
        result += nums[i]

print(result)
