with open('tokens.txt', 'w') as tokens:
    tokens.write('12345 54321')

with open('tokens.txt', 'r') as tokens:
    for lines in tokens:
        token = lines.split()
    print(token[0])
    print(token[1])
