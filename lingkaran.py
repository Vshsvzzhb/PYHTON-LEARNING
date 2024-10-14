def lingkaran():
    r =int(input('masukkan jari jari bola ='))
    phi = 3.14
    luas = lambda r, phi : 4 * phi * r**2
    volume = lambda r, phi :4/3 * phi * r**3

    print("luas bola adalah \t,", luas (r, phi))
    print("volume bola adalah \t", volume (r, phi))

lingkaran()
lingkaran()
lingkaran()