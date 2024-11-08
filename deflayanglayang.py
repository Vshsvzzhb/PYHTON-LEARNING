def luas_layang_layang (diagonal1, diagonal2):
    return 0,5 * diagonal1 * diagonal2

def keliling_layang_layang (sisi1, sisi2):
    return 2 * (sisi1 + sisi2)

diagonal1 = float(input("masukkan panjang diagonal 1 layang - layang:"))
diagonal2 = float(input("masukkan panjang diagonal 2 layang - layang:"))
sisi1 = float(input("masukkan sisi 1 layang - layang: "))
sisi2 = float(input("masukkan sisi 2 layang - layang: "))
print("luas layang layang:",luas_layang_layang(diagonal1, diagonal2))
print("keliling layang layang:", keliling_layang_layang(sisi1, sisi2))