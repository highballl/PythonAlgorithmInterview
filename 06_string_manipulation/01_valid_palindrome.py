from collections import deque
import sys
sentence = sys.stdin.readline().strip().lower()

special_char = "\"\'[!@#$%^&*:()\,]"
new_sentence = deque([])
for word in sentence:
    new_word = word.lower()
    for char in new_word:
        if char in special_char or char == ' ':
            pass
        else:
            new_sentence.append(char)
#print(new_sentence)

def is_valid(sentence):
    while new_sentence:
        left = new_sentence.popleft()
        if new_sentence:
            right = new_sentence.pop()
            if left == right:
                pass
            else:
                return "false"
                
    return "true"


    
print(is_valid(new_sentence))  