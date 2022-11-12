from prettytable import PrettyTable
x = PrettyTable()

# input data dan nilai Mahasiswa
nama_295 = str(input("Masukan nama anda = "))
nim_295 = int(input("Masukan nim anda = "))
tugas_295 = int(input("input Nilai tugas anda = "))
uts_295 = int(input("input Nilai UTS anda = "))
uas_295 = int(input("input Nilai UAS anda = "))

# Rumus perhitungan nilai akhir
nilai_295 = 25/100 * tugas_295 + 35/100 * uts_295 + 40/100 * uas_295

# Percabangan grade Nilai akhir
if nilai_295 >= 75:
    grade_295 = "A"
    if nilai_295 < 75:
        grade_295 = "B"
        if nilai_295 < 60:
            grade_295 = "C"
            if nilai_295 < 45:
                grade_295 = "D"

# tabel data dan nilai mahasiswa
x.field_names = ["Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir", "Grade"]
x.add_row([nama_295, nim_295, tugas_295, uts_295,
          uas_295, nilai_295, grade_295])
print(x)
