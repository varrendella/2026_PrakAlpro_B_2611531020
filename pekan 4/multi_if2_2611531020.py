total_belanja_1020 = float(input("masukan total belanja (Rp): "))

input_member_1020 = input("apakah member? (y/t): ").strip().lower()
is_member_1020 = input_member_1020 in ["y", "ya"]

input_promo_1020 =input("apakah kode promovalid? (y/t): ").strip().lower()
kode_promo_valid_1020 = input_promo_1020 in ["y", "ya"]

total_diskon_persen_1020 = 0

if total_belanja_1020 > 1000000:
    total_diskon_persen_1020 += 10

if is_member_1020 :
    total_diskon_persen_1020 += 5

if kode_promo_valid_1020 :
    total_diskon_persen_1020 += 15

nominal_diskon_1020 = total_belanja_1020 = (total_diskon_persen_1020 / 100)
total_bayar_1020 = total_belanja_1020 - nominal_diskon_1020

print("\n---rincian pembayaran ---")
print(f"total diskon_1020 :{total_diskon_persen_1020}% (Rp {nominal_diskon_1020:,.0f})")
print(f"total bayar_1020 : Rp {total_bayar_1020:,.0f}" )

print(f"total diskon yang anda dapatkan: {total_diskon_persen_1020}%")