logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

digit = []
letter = []
count = 0
for log in logs:
    for string in log:
        if string == " ":
            idx = log.index(string)
            break
    identifier = log[:idx]
    rest = log[idx:]
    rest_check = ''.join(rest.split())
    print(rest_check)
    #if identifier.startswith('dig'):
    if rest_check.isdigit():
        digit.append(identifier+rest)
    else:
        letter.append([identifier, rest])
        count += 1

sorted_letter = sorted(letter, key=lambda x: (x[1], x[0]))
letter = [sorted_letter[i][0]+sorted_letter[i][1] for i in range(count)]
print([*letter, *digit])

