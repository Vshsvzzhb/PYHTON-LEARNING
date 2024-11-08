def volume_bola(jari_jari):
    return (4/3) * 22/7 * jari_jari ** 3

def luas_permukaan_bola(jari_jari):
    return 4 * 22/7 * jari_jari ** 2

jari_jari = float(input("masukkan jari jari bola:"))

print("volume bola:", volume_bola(jari_jari))         
print("luas permukaan bola:", luas_permukaan_bola(jari_jari)) 
