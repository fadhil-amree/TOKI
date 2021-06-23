bil = list(map(int, input().split(' ')))
naik = sorted(bil[:3])
if bil[3] == 1:
    for i in naik:
        print(i , end= ' ')
else:
    turun = naik[::-1]
    for j in turun:
        print(j, end=' ')
    
    