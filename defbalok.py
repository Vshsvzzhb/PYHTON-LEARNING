def volume_balok (panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def luas_permukaan_balok (panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

panjang = float(input("masukkan panjang balok: "))
lebar = float(input("masukkan lebar balok: "))
tinggi = float(input("masukkan tinggi balok"))

print("volume balok", volume_balok(panjang, lebar, tinggi))
print("luas peermukaan balok", luas_permukaan_balok(panjang, lebar, tinggi))