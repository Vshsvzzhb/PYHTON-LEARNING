import random

def game_tebak_angka():
    angka = random.randint(1, 100)
    kesempatan = 5

    while kesempatan > 0:
        tebak = int(input("Tebak angka (1-100): "))
        if tebak == angka:
            print("Anda menang!")
            break
        elif tebak < angka:
            print("Terlalu rendah!")
        else:
            print("Terlalu tinggi!")
        kesempatan -= 1

    if kesempatan == 0:
        print(f"Game over! Angka adalah {angka}")

game_tebak_angka()
