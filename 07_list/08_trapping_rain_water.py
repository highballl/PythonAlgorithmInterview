# height = [0,1,0,2,1,0,1,3,2,1,2,1]

# # do not sort
# l = len(height)
# max_num = max(height)
# i = 1
# idx = []
# counts = []
# while i <= max_num:
#     temp = []
#     temp.append(height.index(i))
#     count = 1
#     for j in reversed(range(l)):
#         if height[j] == i and j not in temp:
#             temp.append(j)
#             count += 1
#             #break
#     if len(temp) > 0:
#         #temp.append(count)
#         idx.append(temp)
#         counts.append(count)
#     i += 1

# #print(idx)
# #print(counts)
# result = 0
# for i in range(len(idx)):
#     if len(idx[i]) > 1:
#         length = idx[i][1] - idx[i][0]
#         result += (length - 1) - len(counts[i:]) - 2
#     elif len(idx[i]) == 0 and idx[i] == max_num:
#         result -= 1

# print(result)



# error case
# height = [4,2,0,3,2,5]
# 1 is not in list
# 값이 없는 경우 예외처리를 안했다.
height = [0,1,0,2,1,0,1,3,2,1,2,1]

l = len(height)
max_num = max(height)
max_idx = height.index(max_num)

count = 0
temp_max = 0
for i in range(max_idx):
    if height[i] > temp_max:
        temp_max = height[i]
    count += temp_max - height[i]
    #print('loop',i)
    #print('left', count)

temp_max = 0
for j in range(l-1, max_idx-1, -1):
    if height[j] > temp_max:
        temp_max = height[j]
    count += temp_max - height[j]
    #print('loop',j)
    #print('right', count)


print(count)