l_strings = []

while True:
    string = input().strip()

    if string.lower()=='fim':
        break
    elif string[0]=='a':
        l_strings.append(string)
    
for i in l_strings:
    print(i)