def penghitung_bmi():
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))

    bmi = berat / (tinggi ** 2)

    if bmi < 18.5:
        print("Berat badan kurang")
    elif bmi < 25:
        print("Berat badan normal")
    elif bmi < 30:
        print("Berat badan berlebih")
    else:
        print("Obesitas")

penghitung_bmi()