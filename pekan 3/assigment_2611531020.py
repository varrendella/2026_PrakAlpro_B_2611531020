angka1 = int(input("input angka-1: "))
angka2 = int(input("input angka-2: "))

print("\nNilai awal angka1 =", angka1)
print("Nilai awal angka2 =", angka2)

hasil = angka1
print("\Assigment biasa (=)")
print("hasil =", hasil)

hasil = angka1
hasil += angka2
print("\nAssigment penambahan (+=)")
print("hasil =", hasil)

hasil = angka1
hasil -= angka2
print("\nAssigment pengurangan (-=)")
print("hasil =", hasil)

hasil = angka1
hasil *= angka2
print("\nAssigment perkalian (*=)")
print("hasil =", hasil)

if angka2 != 0:
    hasil = angka1
    hasil //= angka2
    print("\nAssigment pembagian  (/=)")
    print("hasil =", hasil)
    hasil = angka1
    hasil //= angka2
    print("\nAssigment pembagian bulat (//=)")
    print("hasil =", hasil)
    hasil = angka1
    hasil %= angka2
    print("\nAssigment sisa bagi (%=)")
    print("hasil =", hasil)
else:
    print("\Pembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

hasil = angka1
hasil **= angka2
print("\nAssigment pangkat (**=)")
print("hasil =", hasil)
