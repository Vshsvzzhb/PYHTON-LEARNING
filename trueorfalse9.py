tahun = int(input("Masukkan tahun: "))
print((tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)) 