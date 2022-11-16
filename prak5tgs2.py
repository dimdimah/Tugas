from prettytable import PrettyTable
x = PrettyTable()

# data gaji pokok karyawan
gapok_a = 500000
gapok_b = 700000
gapok_c = 900000

# rumus menentukan tunjangan karyawan
tunjangan_A = 500000 + (500000 * 10) / 100
tunjangan_B = 700000 + (700000 * 15) / 100
tunjangan_C = 900000 + (900000 * 20) / 100

# input data karyawan pt. xyz
print("PROGRAM PERHITUNGAN GAJI KARYAWAN")
print("============================================")
print()
nama_295 = (input("Tulis Nama Anda = "))
golongan_295 = (input("Masukan Golongan kerja anda = "))
ttl_jamKerja_295 = int(input("total jam kerja anda selama 1 bulan = "))

# Rumus cari lembur
lembur_a = (ttl_jamKerja_295 - 200) * 5000
lembur_b = (ttl_jamKerja_295 - 200) * 7500
lembur_c = (ttl_jamKerja_295 - 200) * 10000

# rumus cari gaji bersih/gaji total
gatot_295_a = gapok_a + tunjangan_A + lembur_a
gatot_295_b = gapok_a + tunjangan_A + lembur_a
gatot_295_c = gapok_a + tunjangan_A + lembur_a

print("==========================================================")
print("================Hasil Perhitungan gaji anda===============")

# perhitungan lembur karyawan /jam
if golongan_295 == 'a':
    print()
    if ttl_jamKerja_295 >= 200:
        x.field_names = ["Golongan", "Gaji Pokok",
                         "Tunjangan", "Upah Lembur", "Gaji Total"]
        x.add_row([golongan_295, "Rp 500.000",
                  tunjangan_A, lembur_a, gatot_295_a])
        print(x)
    else:
        x.field_names = ["Golongan", "Gaji Pokok",
                         "Tunjangan", "Upah Lembur", "Gaji Total"]
        x.add_row([golongan_295, "Rp 500.000",
                  tunjangan_A, "Tidak Ada", gatot_295_a])
        print(x)
elif golongan_295 == 'b':
    print()
    if ttl_jamKerja_295 >= 200:
        x.field_names = ["Golongan", "Gaji Pokok",
                         "Tunjangan", "Upah Lembur", "Gaji Total"]
        x.add_row([golongan_295, "Rp 700.000",
                  tunjangan_B, lembur_b, gatot_295_b])
        print(x)
    else:
        x.field_names = ["Golongan", "Gaji Pokok",
                         "Tunjangan", "Upah Lembur", "Gaji Total"]
        x.add_row([golongan_295, "Rp 700.000",
                  tunjangan_B, "Tidak Ada", gatot_295_b])
        print(x)
elif golongan_295 == 'c':
    print()
    if ttl_jamKerja_295 >= 200:
        x.field_names = ["Golongan", "Gaji Pokok",
                         "Tunjangan", "Upah Lembur", "Gaji Total"]
        x.add_row([golongan_295, "Rp 900.000",
                  tunjangan_C, lembur_c, gatot_295_c])
        print(x)
    else:
        x.field_names = ["Golongan", "Gaji Pokok",
                         "Tunjangan", "Upah Lembur", "Gaji Total"]
        x.add_row([golongan_295, "Rp 900.000",
                  tunjangan_C, "Tidak Ada", gatot_295_c])
        print(x)
