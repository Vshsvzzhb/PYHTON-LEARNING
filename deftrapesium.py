def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    return 0,5 * (sisi_atas + sisi_bawah + tinggi)

def keliling_trapesium(sisi_atas, sisi_bawah, sisi_miring1, sisi_miring2):
    return sisi_atas + sisi_bawah + sisi_miring1 + sisi_miring2

sisi_atas = float(input("masukkan panjang sisi atas trapesium:"))
sisi_bawah = float(input("masukkan panjang sisi bawah trapesium:"))
tinggi = float(input("masukkan tinggi trapesium:"))
sisi_miring1 = float(input("masukkan panjang sisi miring 1 trapesium:"))
sisi_miring2 = float(input("masukkan panjang sisi miring 2 trapesium: "))

print("luas trapesium", luas_trapesium(sisi_atas, sisi_bawah, tinggi))
print("keliling trapesium", keliling_trapesium(sisi_atas, sisi_bawah, sisi_miring1, sisi_miring2))