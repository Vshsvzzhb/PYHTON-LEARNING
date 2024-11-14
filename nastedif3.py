angka = int(input("Masukkan angka: "))
if angka % 2 == 0:
    if angka > 0:
        print("Angka genap dan positif.")
    elif angka < 0:
        print("Angka genap dan negatif.")
    else:
        print("Angka genap dan nol.")
else:
    if angka > 0:
        print("Angka ganjil dan positif.")
    elif angka < 0:
        print("Angka ganjil dan negatif.")
    else:
        print("Angka ganjil dan nol.")