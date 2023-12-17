var_list = [1, 2, 3, 4, 5]
for i in var_list:
    print(i)
print("\n")

for q in range(5):
    print(q)
print("\n")

for i in range(1, 10, 2):
    print(i)
print("\n")

counter = 1
while counter <= 5:
    print(counter)
    counter += 1
print("\n")

for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
print("\n")

for i in range(2):
    print("Perulangan luar:", i)
    for j in range(10):
        print("Perulangan dalam:", j)
        if j == 1:
            break
print("\n")

for huruf in "Dico ding":
    if huruf == " ":
        continue
    print("Huruf saat ini:", huruf)
print("\n")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan")
print("\n")

count = 0
while count < 3:
    print("Dicoding")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False)")
print("\n")

n = 10
while n > 0:
    n -= 1
    if n == 7:
        break
    print(n)
else:
    print("loop selesai")
print("\n")

x = 10
if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")
print("\n")

angka = [1, 2, 3, 4]
# pangkat = []
# for n in angka:
#     pangkat.append(n**2)
pangkat = [n**2 for n in angka]
print(pangkat)


evenNumber = [i for i in range(0, 502, 2)]
print(evenNumber)
