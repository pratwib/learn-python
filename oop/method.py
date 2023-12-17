def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi")
        func()
        print("Setelah fungsi dieksekusi")

    return wrapper


@my_decorator
def say_hello():
    print("Hello world!")


say_hello()

print("\n")


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

    @staticmethod
    def intro_mobil():
        print("Ini adalah intro metode dari kelas Mobil")

    @classmethod
    def outro_mobil(cls):
        print("Ini adalah outro metode dari kelas Mobil")


mobil_1 = Mobil("Merah", "DicodingCar", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()
print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)

Mobil.intro_mobil()
mobil_1.intro_mobil()

Mobil.outro_mobil()
mobil_1.outro_mobil()
