ketersediaan = "Daging Ayam"
if ketersediaan == "Daging Ayam":
    print("Ibu membeli ayam")
else:
    print("Ibu membeli tempe")

score = 100
if score == 100:
    print("Nilai Anda sempurna!")

x = ""
if x:
    print("Ini True")

skor = 100
if skor == 100:
    print("Nilai Anda bagus!")

tinggi_badan = 120
if tinggi_badan >= 160:
    print("Anda boleh naik")
else:
    print("Anda tidak boleh naik")

nilai = 65
if nilai >= 80:
    print("Selamat! Anda mendapat nilai A")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
elif nilai >= 60:
    print("Hmm.. Anda mendapat nilai C")
else:
    print("Waduh, Anda mendapat nilai D")

nilai = 81
perilaku = "tidak baik"
if nilai >= 80 and perilaku == "baik":
    print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
elif nilai >= 80 and perilaku != "baik":
    print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
else:
    print("Yuk belajar lebih giat lagi!")

# Ternary Operators
lulus = True
print("Selamat") if lulus else print("Coba lagi")

# Ternary Tuples
lulus = False
kelulusan = ("Perbaiki", "Selamat")[lulus]
print(kelulusan)
