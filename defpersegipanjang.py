def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling =2 * (panjang + lebar)
    return luas, keliling

panjang = float(input("masukkan panjang persegi panjang: "))
lebar = float(input("masukkan lebar persegi panjang: "))
luas, keliling = persegi_panjang(panjang, lebar)
print(f"luas persegi panjang: {luas}, keliling persegi panjang: {keliling}")