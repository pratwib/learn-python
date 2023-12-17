kata = "Dicoding"
kata = kata.upper()
print(kata)
kata = kata.lower()
print(kata)

print("Dicoding     ".rstrip())
print("      Dicoding".lstrip())
print("      Dicoding        ".strip())
kata = "CodeCodeDicodingCodeCode"
print(kata.strip("Code"))

print("Dicoding Indonesia".startswith("Dicoding"))
print("Dicoding Indonesia".endswith("Dicoding"))

print(" ".join(["Dicoding", "Indonesia", "!"]))
print("123".join(["Dicoding", "Indonesia"]))
print("Dicoding Indonesia !".split())
print(
    """Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.""".split(
        "\n"
    )
)

string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

kata = "DICODING"
print(kata.isupper())
print(kata.islower())
kata = "dicod1ng"
print(kata.isalpha())
kata = "dicoding123*"
print(kata.isalnum())
print("123".isdecimal())
print("    ".isspace())
print("Dicoding Indonesia".istitle())

teks = "Code"
add_number = teks.zfill(5)
print(add_number)
print("Dicoding".rjust(20))
print("Dicoding".rjust(20, "!"))
print("Dicoding".ljust(20, "!"))
print("Dicoding".center(10, "-"))

st1 = "Jum'at"
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum'at yang lalu.")
print(r"Dicoding\tIndonesia")
