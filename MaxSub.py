name1 = str(input())

with open(name1) as file:
    lines = [line.rstrip() for line in file]

#print(lines)

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    if len(substr)!=0: print(substr)
    else: print('none')
    


long_substr(lines)

