def volume_kubus(sisi):
    return sisi ** 3

def luas_permukaan_kubus(sisi):
    return 6 * (sisi ** 2)

sisi = float(input("masukkan panjang sisi kubus: "))
print("volume kubus", volume_kubus(sisi))
print("luas permukaan kubus", luas_permukaan_kubus(sisi))