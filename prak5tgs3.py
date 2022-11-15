print("Program menghitung luas bidang")
print("==============================")

print(" 1. Menghitung luas persegi panjang \n 2. Menghitung luas lingkaran \n 3. Menghitung luas segitiga")
print()

choice_295 = str(
    input("Kamu mau menghitung luas bidang apa? (pilih angka 1-3) "))

# menghitung luas bidang dengan switch
match choice_295:
    case "1":
        print("kamu ingin Menghitung luas persegi panjang.")
        p = int(input("berapa panjang objeknya? "))
        l = int(input("berapa lebar objeknya? "))
        luas_295 = p * l
        print("luas persegi panjangnya adalah? ", luas_295)
    case "2":
        print("kamu ingin Menghitung luas lingkaran.")
        r = int(input("berapa panjang objeknya? "))
        ling_295 = 3.14 * r * r
        print("luas lingkarannya adalah? ", ling_295)

    case "3":
        print("kamu ingin Menghitung luas Segitiga.")
        a = int(input("berapa alas objeknya? "))
        t = int(input("berapa tinggi objeknya? "))
        luassgt_295 = 0.5 * a * t
        print("luas persegi panjangnya adalah? ", luassgt_295)

    case _:
        print("perhitungan yang kamu cari tidak tertera!")

        print('')
print('=======================================================')
print('terima kasih telah menggunakan program ini.')
