N = int(input())
list = []
tsil = []
lo = []
for i in range (N):
    a = input()
    for y in a:
        lo.append(y)
    li  = lo[::-1]  
    list.append(int( ''.join(li)))
    lo = []

for x in list:
    print(x)

