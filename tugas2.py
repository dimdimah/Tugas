from prettytable import PrettyTable
x = PrettyTable()

gapok_a = 500000
gapok_b = 700000
gapok_c = 900000

# rumus menentukan tunjangan karyawan
upah_kotor_A = 500000 + (500000 * 10) / 100
upah_kotor_B = 700000 + (700000 * 15) / 100
upah_kotor_C = 900000 + (900000 * 20) / 100

# input data karyawan pt. xyz
print("PROGRAM PERHITUNGAN GAJI KARYAWAN")
print("============================================")
print()
nama_295 = (input("Tulis Nama Anda = "))
golongan_295 = (input("Masukan Golongan kerja anda = "))
ttl_jamKerja_295 = int(input("total jam kerja anda selama 1 bulan = "))

lembur_a = ttl_jamKerja_295 * 5000
lembur_b = ttl_jamKerja_295 * 7500
lembur_c = ttl_jamKerja_295 * 10000
print("=================================================")
print("================Hasil Perhitungan gaji anda===============")

if golongan_295 == 'a':
    print()
    if ttl_jamKerja_295 >= 200:
        x.field_names = ["Golongan", "Gaji Pokok", "Tunjangan", "Upah Lembur"]
        x.add_row([golongan_295, "Rp 500.000", upah_kotor_A, lembur_a])
        print(x)
    else:
        x.field_names = ["Golongan", "Gaji Pokok", "Tunjangan", "Upah Lembur"]
        x.add_row([golongan_295, "Rp 500.000", upah_kotor_A, "Tidak Ada"])
        print(x)
elif golongan_295 == 'b':
    print()
    if ttl_jamKerja_295 >= 200:
        x.field_names = ["Golongan", "Gaji Pokok", "Tunjangan", "Upah Lembur"]
        x.add_row([golongan_295, "Rp 700.000", upah_kotor_B, lembur_b])
        print(x)
    else:
        x.field_names = ["Golongan", "Gaji Pokok", "Tunjangan", "Upah Lembur"]
        x.add_row([golongan_295, "Rp 700.000", upah_kotor_B, "Tidak Ada"])
        print(x)

elif golongan_295 == 'c':
    print()
    if ttl_jamKerja_295 >= 200:
        x.field_names = ["Golongan", "Gaji Pokok", "Tunjangan", "Upah Lembur"]
        x.add_row([golongan_295, "Rp 900.000", upah_kotor_C, lembur_c])
        print(x)
    else:
        x.field_names = ["Golongan", "Gaji Pokok", "Tunjangan", "Upah Lembur"]
        x.add_row([golongan_295, "Rp 900.000", upah_kotor_C, "Tidak Ada"])
        print(x)

# ================percobaan ke 2=========================
# percabagan gaji karyawan pt. xyz
# if golongan_295 == 'A':
#     print("Gaji Pokok anda adalah Rp.", gapok_a)
#     if ttl_jamKerja_295 >= 200:
#         print("Tunjangan Anda   = Rp.", upah_kotor_A)
#         print("Upah lembur anda = Rp.", lembur_a)
#         print("Total gaji anda  = Rp.", gapok_a + upah_kotor_A + lembur_a)
#     else:
#         print("Upah Lembur     = Tidak ada")
#         print("Total gaji anda = Rp.", gapok_a + upah_kotor_A)
# elif golongan_295 == 'B':
#     print("Gaji Pokok anda adalah Rp.", gapok_b)
#     if ttl_jamKerja_295 >= 200:
#         print("Tunjangan Anda   = Rp.", upah_kotor_B)
#         print("Upah lembur anda = Rp.", lembur_b)
#         print("Total gaji anda  = Rp.", gapok_b + upah_kotor_B + lembur_b)
#     else:
#         print("Upah Lembur     = Tidak ada")
#         print("Total gaji anda = Rp.", gapok_b + upah_kotor_B)
# elif golongan_295 == 'C':
#     print("Gaji Pokok anda adalah Rp.", gapok_c)
#     if ttl_jamKerja_295 >= 200:
#         print("Tunjangan anda   = Rp.", upah_kotor_C)
#         print("Upah lembur anda = Rp.", lembur_c)
#         print("Total gaji anda  = Rp.", gapok_c + upah_kotor_C + lembur_c)
#     else:
#         print("Upah Lembur     = Tidak ada")
#         print("Total gaji anda = Rp.", gapok_c + upah_kotor_C)
# print()
