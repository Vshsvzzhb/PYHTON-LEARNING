nilai = int(input("masukkan nilai:"))

if nilai >= 100:
    grade = "grade A"
elif nilai >= 80:
    grade = "grade B"
elif nilai >= 60:
    grade = "grade C"
elif nilai >= 55:
    grade = "grade D"
else:
    grade = "grade E"

print(f"nilai: {nilai}, grade: {grade}")    