def mencari_luas_persegi_panjang(panjang, lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.
    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.
    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """
    luar_persegi_panjang = panjang * lebar
    return luar_persegi_panjang


persegi_panjang_pertama = mencari_luas_persegi_panjang(10, 5)
print(persegi_panjang_pertama)


def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan


print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))


def penjumlahan(a, b, /):
    return a + b


print(penjumlahan(8, 50))


def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan


print(greeting(pesan="Selamat sore!", nama="Dicoding"))


def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total


print(hitung_total(1, 2, 3))


def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ": " + value + ", "
    return info


print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Programmer"))

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang * lebar
print(mencari_luas_persegi_panjang(4, 9))

a = 10


def add(b):
    result = a + b
    return result


bilanganPertama = add(20)
print(bilanganPertama)


def add(a, b):
    lokal_var = 5
    result = a + b - lokal_var
    return result


bilanganPertama = add(10, 20)
print(bilanganPertama)
