def luas_belah_ketupat (diagonal1, diagonal2):
    return 0,5 * diagonal1 * diagonal2 

def keliling_belah_ketupat(sisi):
    return 4 * sisi

diagonal1 = float(input("masukkan panjang diagonal1 belah ketupat: "))
diagonal2 = float(input("masukkan panjang diagonal2 belah ketupat: "))
sisi = float(input("masukkan panjang sisi belah ketupat: "))

print("luas belah ketupat", luas_belah_ketupat(diagonal1, diagonal2))
print("keliling belah ketupat", keliling_belah_ketupat(sisi))