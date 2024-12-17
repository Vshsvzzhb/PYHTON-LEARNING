import time

def hitung_waktu_nyata():
    start_time = time.time()
    input("Tekan Enter untuk mulai...")
    end_time = time.time()
    waktu_berlalu = end_time - start_time

    menit = int(waktu_berlalu // 60)
    detik = int(waktu_berlalu % 60)

    print(f"Waktu berlalu: {menit} menit, {detik} detik")

hitung_waktu_nyata()
