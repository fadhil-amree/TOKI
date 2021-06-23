ukuran = list(map(int, input().split(' ')))

if ukuran[0] <= 10 and ukuran[1] <=40 and ukuran[2]<= 90:
    print('S')
elif ukuran[0] <= 14 and ukuran[1] <=60 and ukuran[2]<= 120:
    print('M')
elif ukuran[0] <= 18 and ukuran[1] <=80 and ukuran[2]<= 180:
    print('L')
else:
    print('X')