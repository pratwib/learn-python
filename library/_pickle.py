import pickle

contoh_dictionary = {1: "6", 2: "2", 3: "f"}
pickle_keluar = open("dict.pickle", "wb")
pickle.dump(contoh_dictionary, pickle)
pickle_keluar.close()

pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()

print(contohDictionary)
