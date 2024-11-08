def lingkaran (radius):
    luas = 22.7 * radius ** 2
    keliling = 2 * 22.7 * radius
    return luas, keliling

radius = float(input("masukkan jari jari lingkaran: "))
luas, keliling = lingkaran(radius)
print(f"luas lingkaran: {luas}, keliling lingkaran: {keliling}")