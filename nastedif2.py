nilai = int(input("Masukkan nilai ujian: "))
if nilai >= 60:
    if nilai >= 80:
        print("Anda lulus dengan nilai A!")
    elif nilai >= 70:
        print("Anda lulus dengan nilai B!")
    else:
        print("Anda lulus dengan nilai C!")
else:
    print("Anda tidak lulus.")