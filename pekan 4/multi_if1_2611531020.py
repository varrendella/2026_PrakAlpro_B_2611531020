umur_1020 = int(input("input umur anda: "))
sim_1020 = input("apakah anda sudah punya sim C (Y/T): ")[0]

if umur_1020 >= 17 and sim_1020 == 'y':
    print("anda sudah dewasa dan boleh bawa motor ")

if umur_1020 >= 17 and sim_1020 != 'y':
    print("anda sudah dewasa tetapi tidak boleh bawa motor ")

if umur_1020 < 17 and sim_1020 == 'y':
    print("anda belum cukup umur punya sim ")

if umur_1020 < 17 and sim_1020 != 'y':
    print("anda belum cukup umur bawa motor ")
print("program selesai")