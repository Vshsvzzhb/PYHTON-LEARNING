def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

sisi = float(input("masukkan panjang sisi persegi:"))
luas, keliling = persegi (sisi)
print(f"luas persegi :{luas}, keliling persegi: {keliling}")