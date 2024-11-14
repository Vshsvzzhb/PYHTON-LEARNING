tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
tahun_sekarang = 2024
usia = tahun_sekarang - tahun_lahir

if usia >= 18:
    if usia >= 60:
        print("Anda sudah lansia.")
    else:
        print("Anda sudah dewasa.")
else:
    if usia >= 13:
        print("Anda remaja.")
    else:
        print("Anda masih anak-anak.")