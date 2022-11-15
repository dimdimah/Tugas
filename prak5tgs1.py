from prettytable import PrettyTable

x = PrettyTable()

# input data dan nilai Mahasiswa

nama_295 = str(input("Masukan nama anda = "))
nim_295 = int(input("Masukan nim anda = "))
tugas_295 = int(input("input Nilai tugas anda = "))
uts_295 = int(input("input Nilai UTS anda = "))
uas_295 = int(input("input Nilai UAS anda = "))

# Rumus perhitungan nilai akhir
Tugas = int(tugas_295*25/100)
Uts = int(uts_295*35/100)
Uas = int(uas_295*40/100)
nilai_295 = Tugas+Uts+Uas

# tabel data dan nilai mahasiswa
x.field_names = ["Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir", ]
x.add_row([nama_295, nim_295, tugas_295, uts_295, uas_295, nilai_295, ])
print(x)

# Percabangan grade Nilai akhir
if nilai_295 >= 75 and nilai_295 < 100:
    print('GRADE NILAI ANDA = A')
elif nilai_295 >= 70 and nilai_295 < 75:
    print('GRADE NILAI ANDA = B')
elif nilai_295 >= 46 and nilai_295 < 60:
    print('GRADE NILAI ANDA = C')
elif nilai_295 >= 0 and nilai_295 < 45:
    print('GRADE NILAI ANDA = D')
