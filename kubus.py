def kubus():
    sisi = int(input("masukkan sisi kubus :"))

    luas = lambda sisi: 6 * sisi **2
    volume = lambda sisi : sisi**3

    print('nilai volume kubus adalah\t\t: ', volume(sisi))
    print('nilai luas kubus adalah\t\t: ' ,luas(sisi))

kubus()
kubus()
kubus()