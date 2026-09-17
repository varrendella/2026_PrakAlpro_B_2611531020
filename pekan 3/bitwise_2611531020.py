print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_1020 = int(input("Masukan angka bitwise-1: "))
angka1_1020 = int(input("Masukan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_1020 - Desimal:", angka1_1020, "| - biner:", bin(angka1_1020))
print("angka2_1020 - Desimal:", angka1_1020, "| - biner:", bin(angka1_1020))

hasil = angka1_1020 & angka1_1020
print("\nBitwise AND (&)")
print(angka1_1020, "&", angka1_1020, "=", hasil)
print("Biner Hasil =", bin(hasil))
print("Biner Hasil (8 bit)=", format(hasil, '08b'))

hasil = angka1_1020 | angka1_1020
print("\nBitwise OR (|)")
print(angka1_1020, "|", angka1_1020, "=", hasil)
print("Biner Hasil =", bin(hasil))
print("Biner Hasil (8 bit)=", format(hasil, '08b')) 

hasil = angka1_1020 ^ angka1_1020
print("\Bitwise XOR (^)")  
print(angka1_1020, "^", angka1_1020, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

hasil = ~angka1_1020
print("\Bitwise NOT (~)")
print("~", angka1_1020, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

jumlah_geser = int(input("\nMasukan jumlah pergeseran bit: "))
hasil = angka1_1020 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_1020, "<<", bin (hasil))
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

jumlah_geser = int(input("\nMasukan jumlah pergeseran bit: "))
hasil = angka1_1020 << jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_1020, ">>", bin (hasil))
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))


