# import hello
from hello import mencari_luas_persegi_panjang, nama


persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

print(nama)


def minimal(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return a


print(minimal(1, 3))
