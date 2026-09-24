umur_1020 = int(input("input umur anda"))
sim_1020 = input("apakah anda sudah boleh punya SIM C: ")[0]

if umur_1020 >= 17 and sim_1020 == 'y':
    print("anda sudah dewasa dan boleh bawa motor ")
elif umur_1020 >= 17 and sim_1020 != 'y':
    print("anda sudah dewasa tetapi tidak boleh bawa motor ")
elif umur_1020 < 17 and sim_1020 == 'y':
    print("anda belum cukup umur punya sim ")
else: 
     print("anda belum cukup umur dan tidak boleh bawa motor ")
print("program selesai")