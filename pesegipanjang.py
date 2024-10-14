def persegipanjang ():
    panjang =int(input("masukkan nilai sisi \t:"))
    lebar =int(input("masukkan nilai sisi \t:"))

    luas= lambda panjang, lebar: panjang * lebar
    keliling = lambda panjang, lebar: 2 * (panjang + lebar)

    print('luas\t\t: ',luas(panjang,lebar), 'cm2')
    print('keliling\t\t: ',keliling(panjang,lebar), 'cm2')

persegipanjang()
persegipanjang()
persegipanjang()
