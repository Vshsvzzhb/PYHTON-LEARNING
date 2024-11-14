pendapatan = int(input("Masukkan pendapatan bulanan Anda: "))
if pendapatan < 1000000:
    if pendapatan < 500000:
        print("Pendapatan Anda sangat rendah.")
    else:
        print("Pendapatan Anda cukup rendah.")
else:
    if pendapatan < 5000000:
        print("Pendapatan Anda menengah.")
    else:
        print("Pendapatan Anda tinggi.")