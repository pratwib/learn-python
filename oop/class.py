class Mobil:
    warna = "Merah"


mobil_1 = Mobil()
print(mobil_1.warna)

mobil_1.warna = "Biru"
print(mobil_1.warna)

mobil1 = Mobil()
print(mobil1.warna)
mobil2 = Mobil()
print(mobil2.warna)
Mobil.warna = "Hitam"
print(mobil1.warna)
print(mobil2.warna)
print("\n")


class Mobil:
    def __init__(self):
        self.warna = "Kuning"


mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hijau"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)
print("\n")


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan


mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)
