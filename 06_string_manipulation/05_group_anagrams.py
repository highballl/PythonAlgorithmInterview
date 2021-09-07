from collections import Counter

strs = ["eat","tea","tan","ate","nat","bat"]

if strs == [""]:
    #return [[""]]
    print([[""]])
        
temp = [ []*i for i in range(len(strs))]
counts = []
result = []
        
for word in strs:
    count = Counter(word)
    if count not in counts:
        counts.append(count)
        idx = counts.index(count)
        temp[idx].append(word)
    else:
        idx = counts.index(count)
        temp[idx].append(word)


for arr in temp:
    if len(arr) != 0:
        result.append(arr)

print(result)