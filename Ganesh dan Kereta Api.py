n = int(input())
nomor = list(map(int,input().split(' ')))
for i in range(n):
    if i != n-1:    
        print(nomor[n-1 -i], end=',')
    else:
        print(nomor[0])