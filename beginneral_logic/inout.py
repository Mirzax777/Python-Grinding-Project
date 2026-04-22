def main():
    nama = input("Nama : ")
    umur = int(input("Umur :"))
    gender = input("Gender : ")

    tinggi = int(input("Tinggi : "))
    berat = int(input("Berat : "))

    if gender.lower() == "pria":
        BMI = berat / (tinggi * tinggi)
    else:
        BMI = berat / (tinggi * tinggi) + 10

    print(nama)
    print(umur)
    print(gender)


if __name__ == '__main__':
    main()
