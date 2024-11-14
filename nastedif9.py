nilai_tugas = int(input("Masukkan nilai tugas: "))
nilai_ujian = int(input("Masukkan nilai ujian: "))

if nilai_tugas >= 60:
    if nilai_ujian >= 70:
        print("Anda lulus!")
    else:
        print("Anda tidak lulus karena nilai ujian kurang.")
else:
    print("Anda tidak lulus karena nilai tugas kurang.")