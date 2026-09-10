# Buat file dengan nama Konstanta_2611531020.py
# Program ini menggunakan Konstanta untuk menghitung luas linggggkaran 
# nama variabel ditambah 4 digitnim terakhir contoh : varren_1020

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_1234 = float(input('Masukan nilai jari-jari: '))
luas_1234 = PI * jari_1234 * jari_1234
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1234, luas_1234))