K, C, A = input().split(' ')
k = int(K)


batik = [[C for i in range(k)]for j in range(k)]
for x in range(k):
    batik[x][x] = A
    batik[k-1-x][x] = A

for c in range(k):
    for d in range(k):
        
        if d == k-1:
            print(batik[c][d])
        else:
            print(batik[c][d], end='')