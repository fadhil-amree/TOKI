pw = input()
al = 0
num = 0
uc = 0
lc = 0
sc = 0

for i in pw:
    if i.islower():
        lc += 1
    if i.isupper():
        uc += 1
    if i.isalpha():
        al += 1
    if i == '?' or i == '!' or i == '_':
        sc += 1
    if i.isnumeric():
        num += 1
if uc >= 1 and lc >= 1 and sc >= 1 and num >=1 and len(pw) >= 8:
    print('Kuat')
elif al > 12:
    print('AgakKuat')
else:
    print('Lemah')

