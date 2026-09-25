print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_1020 = input("Masukkan Nama Pengunjung        : ").strip()
umur_1020 = int(input("Input umur anda                 : "))
sim_c_1020 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].strip().lower()

print()
print("Pilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_1020 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_1020 = int(input("Masukkan jumlah tiket           : "))

if jumlah_tiket_1020 <= 0:
    print("Jumlah tiket tidak valid!")
    exit()

member_1020 = input("Apakah Anda member? (y/t)       : ")[0].strip().lower()
promo_1020 = input("Apakah kode promo valid? (y/t)  : ")[0].strip().lower()

wahana_1020 = ""
harga_satuan_1020 = 0

print()
print("--- KELAYAKAN PENGENDARA WAHANA ---")

match paket_1020:
    case 1:  
        wahana_1020 = "Wahana Safari Rimba"
        harga_satuan_1020 = 50000
        if umur_1020 >= 10:
            status_akses_1020 = "Anda memenuhi syarat umur untuk wahana ini."
        else:
            status_akses_1020 = "Maaf, umur Anda belum mencukupi untuk wahana ini (minimal 10 tahun)."

    case 2:  
        wahana_1020 = "Wahana Arung Jeram"
        harga_satuan_1020 = 75000
        if umur_1020 >= 10:
            status_akses_1020 = "Anda memenuhi syarat umur untuk wahana ini."
        else:
            status_akses_1020 = "Maaf, umur Anda belum mencukupi untuk wahana ini (minimal 10 tahun)."

    case 3:  
        wahana_1020 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1020 = 120000
        if umur_1020 >= 17 and sim_c_1020 == 'y':
            status_akses_1020 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
        elif umur_1020 >= 17 and sim_c_1020 != 'y':
            status_akses_1020 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
        elif umur_1020 < 17 and sim_c_1020 == 'y':
            status_akses_1020 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
        else:
            status_akses_1020 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."

    case 4: 
        wahana_1020 = "Wahana Roller Coaster Kilat"
        harga_satuan_1020 = 100000
        if umur_1020 >= 10:
            status_akses_1020 = "Anda memenuhi syarat umur untuk wahana ini."
        else:
            status_akses_1020 = "Maaf, umur Anda belum mencukupi untuk wahana ini (minimal 10 tahun)."

    case 5:  
        wahana_1020 = "Wahana All-Access VIP"
        harga_satuan_1020 = 220000
        if umur_1020 >= 10:
            status_akses_1020 = "Anda memenuhi syarat umur untuk wahana ini."
        else:
            status_akses_1020 = "Maaf, umur Anda belum mencukupi untuk wahana ini (minimal 10 tahun)."

    case _: 
        print("Paket wahana tidak valid!")
        exit()

print(f"Status Akses: {status_akses_1020}")

subtotal_1020 = harga_satuan_1020 * jumlah_tiket_1020
total_diskon_persen_1020 = 0

if subtotal_1020 >= 200000:
    total_diskon_persen_1020 += 10  

if member_1020 in ["y", "ya"]:
    total_diskon_persen_1020 += 5  

if promo_1020 in ["y", "ya"]:
    total_diskon_persen_1020 += 15  

if jumlah_tiket_1020 >= 5:
    total_diskon_persen_1020 += 5  

nominal_diskon_1020 = subtotal_1020 * (total_diskon_persen_1020 / 100)
total_bayar_1020 = subtotal_1020 - nominal_diskon_1020

print()
print("--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_1020:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_1020}% (Rp {nominal_diskon_1020:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_1020:,.0f}")

if total_bayar_1020 > 300000:
    catatan_layanan_1020 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_1020 = "Terima kasih telah berkunjung."

print(f"Catatan Layanan  : {catatan_layanan_1020}")
print()
print("Program Selesai")
