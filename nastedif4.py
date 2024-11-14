num = int(input("Masukkan angka: "))
if num > 1:
    if all(num % i != 0 for i in range(2, num)):
        print(f"{num} adalah bilangan prima.")
    else:
        print(f"{num} bukan bilangan prima.")
else:
    print(f"{num} bukan bilangan prima.")