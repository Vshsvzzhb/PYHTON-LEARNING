def luas_segitiga(alas, tinggi):
    return 0,5 * alas * tinggi

def keliling_segitiga(sisi1,sisi2,sisi3):
    return sisi1 + sisi2 + sisi3

alas = float(input("masukkan alas segitiga: "))
tinggi = float(input("masukkan tinggi segitiga: "))
sisi1 = float(input("masukkan sisi1 segitiga: "))
sisi2 = float(input(":masukkan sisi2 segitiga: "))
sisi3 = float(input("masukkan sisi3 segitiga: "))
print("luas segitiga:", luas_segitiga(alas, tinggi))
print("keliling segitiga:", keliling_segitiga(sisi1, sisi2, sisi3))