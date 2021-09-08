from collections import deque

#nums = [2, 7, 11, 15]
#target = 9
# nums = [3, 3]
# target = 6

# brute force


# optimization 1
# filtered = deque(sorted([num for num in nums if num < target]))
# temp = 0
# while temp != target:
#     left = filtered.popleft()
#     right = filtered.pop()
#     if left+right == target:
#         print(sorted([nums.index(left), nums.index(right)]))
#         break
# error case
# [3, 3]
# output [0, 0]
# expected [0, 1]

# optimization 2
# filtered = deque(sorted([num for num in nums if num < target]))
# temp = 0
# while temp != target:
#     left = filtered.popleft()
#     right = filtered.pop()
#     if left+right == target:
#         if left == right:
#             print([idx for idx, val in enumerate(nums) if val == left][:2])
#             break
#         print(sorted([nums.index(left), nums.index(right)]))
        # break
# error case
# nums = [3, 2, 3]
# target = 6
# empty deque!

# optimization 3
# from collections import deque


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         filtered = sorted([num for num in nums if num < target])

#         i = 0
#         j = 0
#         while target:
#             left = filtered[i]
#             right = filtered[-1-j]
#             if left+right == target:
#                 if left == right:
#                     return [idx for idx, val in enumerate(nums) if val == left][:2]
#                     break
#                 return sorted([nums.index(left), nums.index(right)])
#                 break
#             elif left+right > target:
#                 j -= 1
#             elif left+right < target:
#                 i += 1

# error case 3
# nums = [0, 4, 3, 0]
# target = 0

# optimization 4
# time limit exceeded
# filtered = sorted([num for num in nums if num <= target])

# i = 0
# j = 0
# left = -1
# right = -1
# l = len(filtered)

# while left+right != target:
#     left = filtered[(-1-i) % l]
#     right = filtered[j % l]
#     if left+right == target:
#         if left == right:
#             print([idx for idx, val in enumerate(nums) if val == left][:2])
#             break
#         print(sorted([nums.index(left), nums.index(right)]))
#         break
#     elif left+right > target:
#         j -= 1
#     elif left+right < target:
#         i += 1

# error case
# nums = [3, 2, 3]
# target = 6

# optimization 5
# filtered = deque(sorted([num for num in nums if num <= target]))
# temp = 0
# while temp != target:
#     left = filtered[0]
#     right = filtered[-1]
#     if left+right == target:
#         if left == right:
#             print([idx for idx, val in enumerate(nums) if val == left][:2])
#             break
#         print(sorted([nums.index(left), nums.index(right)]))
#         break
#     elif left+right > target:
#         filtered.pop()
#     # left + right < target
#     else: 
#         filtered.popleft()

# error case
# nums = [0, 4, 3, 0]
# target = 0

# optimization 6
# filtered = deque(sorted([num for num in nums if num <= target]))
# print(filtered)
# while filtered:
#     left = filtered[0]
#     right = filtered[-1]
#     if left+right == target:
#         if left == right:
#             print([idx for idx, val in enumerate(nums) if val == left][:2])
#             break
#         print(sorted([nums.index(left), nums.index(right)]))
#         break
#     elif left+right > target:
#         filtered.pop()
#     # left + right < target
#     else: 
#         filtered.popleft()




# error case
nums = [-3, 4, 3, 90]
target = 0

# optimization 7 - pass
filtered = deque(sorted(nums))
while filtered:
    left = filtered[0]
    right = filtered[-1]
    if left+right == target:
        if left == right:
            print([idx for idx, val in enumerate(nums) if val == left][:2])
            break
        print(sorted([nums.index(left), nums.index(right)]))
        break
    elif left+right > target:
        filtered.pop()
    # left + right < target
    else: 
        filtered.popleft()

