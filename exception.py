z = 0
try:
    print(1 / z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai 0")
print('\n')

var_dict = {"rata_rata": "1.0"}
try:
    print(f'rata-rata adalah {var_dict['rata_rata']/2}')
except KeyError:
    print('Key tidak ditemukan')
except TypeError:
    print('Anda tidak bisa membagi nilai dengan tipe data string')
else:
    print('Kode ini dieksekusi jika tidak ada exception')
finally:
    print('Kode ini dieksekusi terlepas dari ada atau tidaknya exception')
print('\n')

var = -1
if var<0:
    raise ValueError('Bilangan negatif tidak diperbolehkan')
else:
    for i in range(var):
        print(i+1)
