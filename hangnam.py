import random


kata = ['apel', 'banana', 'mangga', 'jeruk', 'anggur']

kata_terpilih = random.choice(kata)

nyawa = 6

huruf_tertebak = ['_'] * len(kata_terpilih)

print("Selamat datang di game Hangman!")
print("Kata memiliki", len(kata_terpilih), "huruf.")

while nyawa > 0 and '_' in huruf_tertebak:
    print(' '.join(huruf_tertebak))
    huruf = input("Tebak huruf: ").lower()

    if len(huruf) != 1:
        print("Masukkan satu huruf saja!")
    elif huruf in huruf_tertebak:
        print("Huruf sudah ditebak!")
    elif huruf not in kata_terpilih:
        nyawa -= 1
        print(f"Inkorrek! Nyawa tersisa: {nyawa}")
    else:
        for i, huruf_kata in enumerate(kata_terpilih):
            if huruf_kata == huruf:
                huruf_tertebak[i] = huruf

if '_' not in huruf_tertebak:
    print(' '.join(huruf_tertebak))
    print("Selamat, Anda menang!")
else:
    print(f"Anda kalah! Kata yang benar adalah {kata_terpilih}.")
