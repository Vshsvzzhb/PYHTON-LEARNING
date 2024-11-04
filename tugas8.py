#2 + 4 + 6 + 8 + 10 = 30
jumlah = 0
for a in range (2,11,2):
    if a < 10:
        print(a, end=' + ')
    else:
        print(a, end=" = ")
    jumlah=jumlah + (a)
print(jumlah)