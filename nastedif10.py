a = int(input("Masukkan panjang sisi pertama segitiga: "))
b = int(input("Masukkan panjang sisi kedua segitiga: "))
c = int(input("Masukkan panjang sisi ketiga segitiga: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga tersebut adalah segitiga sama sisi.")
    elif a == b or a == c or b == c:
        print("Segitiga tersebut adalah segitiga sama kaki.")
    else:
        print("Segitiga tersebut adalah segitiga sembarang.")
else:
    print("Ketiga sisi tidak membentuk segitiga.")