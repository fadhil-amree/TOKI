T = int(input())

case = []
count = 0

for i in range(T):
    c = int(input())
    if c == 1:
        list = int(input())
        if list< 60:
                count+=1
        case.append(count)
        count = 0
    else:
        list = input().split(' ')
        for z in list:
            if int(z) < 60:
                count+=1
        case.append(count)
        count = 0       
    

for c in range (len(case)):
    print(f'Case #{c+1}: {case[c]}')

