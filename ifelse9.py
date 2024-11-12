num = int(input("Masukkan angka: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} bukan bilangan prima")
            break
    else:
        print(f"{num} adalah bilangan prima")
else:
    print(f"{num} bukan bilangan prima")
