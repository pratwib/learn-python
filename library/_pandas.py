import pandas as pd

# Membuat DataFrame dari dictionary
data = {
    "Nama": ["John", "Jane", "Bob", "Alice"],
    "Usia": [25, 30, 22, 28],
    "Pekerjaan": ["Engineer,", "Teacher", "Designer", "Doctor"],
}

df = pd.DataFrame(data)
print(df)
