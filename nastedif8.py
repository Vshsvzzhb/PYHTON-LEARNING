total_pembelian = float(input("Masukkan total pembelian: "))
if total_pembelian > 0:
    if total_pembelian > 100000:
        print("Diskon 20% diberikan.")
        total_pembelian *= 0.8
    elif total_pembelian > 50000:
        print("Diskon 10% diberikan.")
        total_pembelian *= 0.9
    else:
        print("Tidak ada diskon.")
    print(f"Total pembelian setelah diskon: {total_pembelian}")
else:
    print("Total pembelian tidak valid.")