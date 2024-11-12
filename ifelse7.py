berat = float(input("masukkan berat paket (kg):"))

if berat <= 1:
    biaya = 5000
elif berat <= 5:
    biaya = 8000
elif berat <= 10:
    biaya = 12000
else:
    biaya = 20000

print(f"biaya pengiriman adalah Rp {biaya}")