contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))

contoh_set = {1, 3, 3, 5, 5, 5, 7, 9}
print(contoh_set)
print(len(contoh_set))

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

print("Dicoding" in string)
print("tidak" not in string)

data = ["shirt", "white", "L"]
apparel, color, size = data
print(data)
print(apparel)
print(color)
print(size)

kendaraan = ["motor", "mobil", "heli", "pesawat"]
kendaraan.sort()
print(kendaraan)
kendaraan.sort(reverse=True)
print(kendaraan)
kendaraan = ["motor", "mobil", "heli", "Pesawat"]
kendaraan.sort()
print(kendaraan)
