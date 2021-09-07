from collections import Counter
import re

# TEST CASES
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#paragraph = "Bob. hIt, baLl"
#paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["hit"]
#banned = ["bob", "hit"]
#banned = ["a"]

result = []
words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split()]
for word in words:

    if word not in banned:
        result.append(word)

counter_word = Counter(result)
print(counter_word.most_common(1)[0][0])

