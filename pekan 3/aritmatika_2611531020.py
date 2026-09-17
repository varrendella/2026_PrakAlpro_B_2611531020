angka1 = int(input("input angka-1: "))
angka2 = int(input("input angka-2: "))

hasil = angka1 + angka2
print("\nOperator Penjumlahan")
print("Hasil =", hasil)

hasil = angka1 - angka2
print("\nOperator Pengurangan")
print("Hasil =", hasil)

hasil= angka1 * angka2
print("\nOperator Perkalian")
print("Hasil =", hasil)

if angka2 != 0:
    hasil = angka1 / angka2
    print("\nOperator Pembagian")
    print("Hasil =", hasil)

    hasil = angka1 // angka2
    print("\nOperator Pembagian bulat")
    print("Hasil =", hasil)

    hasil = angka1 % angka2
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak boleh bernilai 0.")

hasil = angka1 ** angka2
print("\nOperator Pangkat")
print("Hasil =", hasil)