# IMAGE

import os
import math


def gambar():
    image = '''
                    ⡠⡀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⡠⡄⠀⠀⠀⠀
            ⠀⠀⢀⡀⠀⠈⠎⡁⠇⠀⢀⣴⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠇⣉⠜⠀⠀⠀
            ⠀⠐⠾⠇⠀⣠⢄⣈⠀⣰⣿⣿⡟⣏⣿⢿⡿⣿⣿⣿⣧⠀⠈⠀⠀⠀⠀⠀
            ⠀⠀⠀⢀⣼⣿⣤⣶⣷⣿⣿⣿⠒⢿⣿⡣⣧⣘⣿⣿⣿⣦⡎⢹⣷⡆⠀⠀
            ⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡟⢁⣀⡈⠙⠻⠟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀
            ⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠁⠀⠀⠶⣄⢹⣿⣿⣧⣿⣿⣿⣿⣿⠀
            ⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠰⡒⢦⠀⠀⢀⣾⣿⣿⢹⣿⣿⣿⣿⣿⡀
            ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠆⠬⢤⣤⣴⣿⣿⣿⣿⡗⢻⣿⣿⣿⣿⡇
            ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⢄⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
            ⠘⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏
            ⠀⠀⠀⠀⠈⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠁
            ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠉⠁⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠟⠛⠿⠿⠿⠟⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀'''

    print(image)


# WELCOME


pAngka = [' PENJUMLAHAN ', ' PENGURANGAN ', ' PERKALIAN ',
          ' PEMBAGIAN ', ' PERPANGKATAN ', ' MODULUS ']

pOperasi = [' PERHITUNGAN ANGKA ', ' LUAS BANGUN DATAR ',
            'KELILING BANGUN DATAR', ' VOLUME BANGUN RUANG ']

pDatar = [' LUAS PERSEGI ', ' LUAS PERSEGI PANJANG ', ' LUAS LINGKARAN ', 'LUAS JAJAR GENJANG ', 'LUAS TRAPESIUM ',
          ' LUAS LAYANG-LAYANG ', ' BELAH KETUPAT ', ' ELIPS ', ' SEGITIGA ', ' SEGILIMA ', ' SEGIENAM ']

kDatar = [' KELILING PERSEGI ', 'KELILING PERSEGI PANJANG ', 'KELILING LINGKARAN ', ' KELILING JAJAR GENJANG ', ' KELILING TRAPESIUM ',
          ' KELILING LAYANG-LAYANG ', ' KELILING BELAH KETUPAT ', ' KELILING ELIPS ', ' KELILING SEGITIGA ', ' KELILING SEGILIMA ', ' KELILING SEGIENAM ']

pSegitiga = [' SEGITIGA SAMA SISI ', 'SEGITIGA SAMA KAKI ',
             ' SEGITIGAS SIKU-SIKU ', ' SEGITIGA SEMBARANG ']


# CLEAR CONSOLE


def clear():
    return os.system('cls')


clear()

# WELCOME OPERASI FUNCT


def operasi(nomor):
    clear()
    gambar()
    print(50*'-')
    print(pOperasi[nomor - 1].center(50, '='))
    print(50*'-')

# WELCOME HITUNG FUNCT


def hitung(nomor):
    clear()
    gambar()
    print(50*'-')
    print(pAngka[nomor - 1].center(50, '='))
    print(50*'-')

# WELCOME DATAR FUNCT


def datar(nomor):
    clear()
    gambar()
    print(50*'-')
    print(pDatar[nomor - 1].center(50, '='))
    print(50*'-')

# WELCOME KELILING FUNCT


def Keliling(nomor):
    clear()
    gambar()
    print(50*'-')
    print(kDatar[nomor - 1].center(50, '='))
    print(50*'-')


# WELCOME SEGITIGAS FUNCT

def kSegitiga(nomor):
    clear()
    gambar()
    print(50*'-')
    print(pSegitiga[nomor - 1].center(50, '='))
    print(50*'-')

# PAMIT


pengulangan = 1


# def pamit():
#     pilihanPengulangan = (input('Ingin Mengulangi? (y, n) :'))

#     if pilihanPengulangan == 'y':
#         pengulangan += 1
#     elif pilihanPengulangan == 'n':
#         gambar()
#         print('terimakasih'.upper().center(50, '='))

#     else:
#         gambar()
#         print('tutro baca deks'.upper().center(50, '='))

#     return pengulangan

# ENGINE PERHITUNGAN ANGKA


def penjumlahan(angkaPertama, angkaKedua):
    return angkaPertama + angkaKedua


def pengurangan(angkaPertama, angkaKedua):
    return angkaPertama - angkaKedua


def perkalian(angkaPertama, angkaKedua):
    return angkaPertama*angkaKedua


def pembagian(angkaPertama, angkaKedua):
    return angkaPertama/angkaKedua


def perpangkatan(angkaPertama, pangkat):
    return angkaPertama ** pangkat


def modulus(angkaPertama, angkaKedua):
    return angkaPertama % angkaKedua


# ENGINE LUAS BANGUN DATAR

def persegi(sisi):
    return sisi ** 3


def persegiPanjang(panjang, lebar):
    return Panjang*lebar


def segitia(alas, tinggi):
    return (0.5 * alas) * tinggi


def lingkaran(r):
    return 3.14 * r * r


def JajarGenjang(alas, tinggi):
    return alas*tinggi


def Treapesium(alasA, alasB, tinggi):
    return 0.5*tinggi(alasA+alasB)


def Layang(d1, d2):
    return 0.5*d1*d2


def Segiima(sisi):
    return (5 / 4) * sisi ** 2 * (1 / math.tan(math.pi / 5))


def segienam(sisi):
    return (3 * math.sqrt(3) * sisi ** 2) / 2


def elips(r1, r2):
    return math.pi * jari_jari1 * jari_jari2


def bujursangkar(sisi):
    return sisi ** 2


def belahketupat(diagonal1, diagonal2):
    return (diagonal1*diagonal2) / 2

# ENGINE KELILING BANGUN DATAR


def KPersegi(sisi):
    return sisi * 4


def KPersegiPanjang(panjang, lebar):
    return 2 * (panjang+lebar)


def kLingkarang(r):
    return 2*3.14.r


def kJajarGenjang(alasA, alasB):
    return 2 * (alasA+alasB)


def kTrapesium(sisiA, sisiB, sisiC, sisiD):
    return sisiA + sisiB + sisiC + sisiD


def kLayang(sisiBawah, sisiAtas):
    return (sisiAtas*2)+(sisiBawah*2)


def kBelahKetupat(sisi):
    return sisi * 4


def kElips(diameter1, diameter2):
    return 2 * 3.14 * math.sqrt((diameter1 ** 2 + diameter2 ** 2) / 2)


def kSegitigaSamaSisi(sisi):
    return sisi * 3


def kSegitigaSiku(alas, sisi):
    return sisi*2 + alas


def kSegitigaSamaKaki(sisi, alas):
    return 2 * sisi + alas


def kSegitigaSembarang(sisiA, sisiB, sisiC):
    return sisiA + sisiB + sisiC


def kSegilima(sisi):
    return sisi * 5


def kSegienam(sisi):
    return sisi * 6


while pengulangan == 1:
    clear()
    gambar()
    pengulangan -= 1
    print(50*'-')
    print(' WELCOME TO PYTHON KALKULATOR '.center(50, '='))
    print(50*'-')
    print('Masukan Pilihan Operasi')
    print('1. Perhitungan Angka')
    print('2. Luas Bangun Datar')
    print('3. Keliling Bangun Datar')
    print('4. Volume Bangun Ruang')
    print(50*'-')

    WELCOME = int(input('Masukan Pilihan : '))

    match WELCOME:
        case 1:

            # perhitungan angka

            operasi(WELCOME)
            print('Masukan Pilihan Operasi')
            print('1. penjumlahan')
            print('2. pengurangan')
            print('3. perkalian')
            print('4. pembagian')
            print('5. perpangkatan')
            print('6. modulus')
            print(50*'-')

            angka = int(input('Masukan Pilihan : '))
            match angka:
                case 1:
                    hitung(angka)
                    angkaPertama = int(input('masukan angka pertama : '))
                    angkaKedua = int(input('masukan Angka Kedua : '))
                    print('Hasilnya adalah : ' + str(
                        penjumlahan(angkaPertama, angkaKedua)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 2:
                    hitung(angka)
                    angkaPertama = int(input('masukan Angka Pertama :'))
                    angkaKedua = int(input('Masukan Angka Kedua :'))
                    print('Hasilnya adalah :' +
                          str(pengurangan(angkaPertama, angkaKedua)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 3:
                    hitung(angka)
                    angkaPertama = int(input('masukan Angka Pertama :'))
                    angkaKedua = int(input('Masukan Angka Kedua :'))
                    print('Hasilnya adalah :' +
                          str(perkalian(angkaPertama, angkaKedua)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 4:
                    hitung(angka)
                    angkaPertama = int(input('masukan Angka Pertama :'))
                    angkaKedua = int(input('Masukan Angka Kedua :'))
                    print('Hasilnya adalah :' +
                          str(pembagian(angkaPertama, angkaKedua)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 5:
                    hitung(angka)
                    angkaPertama = int(input('masukan Angka Pertama :'))
                    pangkat = int(input('Masukan Pangkat :'))
                    print('Hasilnya adalah :' +
                          str(perpangkatan(angkaPertama, pangkat)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 6:
                    hitung(angka)
                    angkaPertama = int(input('masukan Angka Pertama :'))
                    angkaKedua = int(input('Masukan Angka Kedua :'))
                    print('Hasilnya adalah :' +
                          str(modulus(angkaPertama, angkaKedua)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

        case 2:
            operasi(WELCOME)
            # Luas Bangun Datar
            print(50*'-')
            print('Pilihan Operasi :')
            print('1. Luas Persegi')
            print('2. Luas Persegi Panjang')
            print('3. Luas Lingkaran')
            print('4. Luas Jajar Genjang')
            print('5. Luas Treapesium')
            print('6. Luas Layang-Layang')
            print('7. Luas Belah Ketupat')
            print('8. Luas Elips')
            print('9. Luas Segitia')
            print('10. Luas Segiima')
            print('11. Luas Segienam')
            print(50*'-')
            pilihan = int(input('Masukan Pilihan :'))

            match pilihan:
                case 1:
                    datar(pilihan)
                    sisi = int(input('Masukan Panjang Sisi :'))
                    print('Luasnya adalah :' + str(persegi(sisi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 2:
                    datar(pilihan)
                    panjang = int(input('Masukan Panjang :'))
                    lebar = int(input('Masukan Lebar :'))
                    print('Luasnya adalah :' +
                          str(persegiPanjang(panjang, lebar)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 3:
                    datar(pilihan)
                    r = int(input('Masukan Panjang Jari-Jari :'))
                    print('Luasnya adalah :' + str(lingkaran(r)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 4:
                    datar(pilihan)
                    alas = int(input('Masukan Panjang Alas :'))
                    tinggi = int(input('Masukan Tinggi'))
                    print('Luasnya adalah :' + str(JajarGenjang(alas, tinggi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 5:
                    datar(pilihan)
                    alasA = int(input('Masukan Panjang Alas A :'))
                    alasB = int(input('Masukan panjang Alas B :'))
                    print('Luasnya adalah :' +
                          str(Treapesium(alasA, alasB, tinggi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 6:
                    datar(pilihan)
                    d1 = int(input('Masukan Panjang D1 :'))
                    d2 = int(input('Masukan Panjang D2 :'))
                    print('Luasnya adalah :' + str(Layang(d1, d2)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 7:
                    datar(pilihan)
                    diagonal1 = int(input('Masukan Panjang Diagonal 1:'))
                    diagonal2 = int(input('Masukan Panjang Diagonal 2'))
                    print('Luasnya adalah :' +
                          str(belahketupat(diagonal1, diagonal2)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 8:
                    datar(pilihan)
                    r1 = int(input('Masukan Panjang Jari-Jari 1 :'))
                    r2 = int(input('Masukan Panjang Jari-Jari 2 :'))
                    print('Luasnya adalah :' + str(elips(r1, r2)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 9:
                    datar(pilihan)
                    print('Luas Segitiga'.center(50, ':'))
                    alas = int(input('Masukan Panjang Alas :'))
                    tinggi = int(input('Masukan Tinggi :'))
                    print('Luasnya adalah :' + str(segitia(alas, tinggi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 10:
                    datar(pilihan)
                    sisi = int(input('Masukan Panjang Sisi:'))
                    print('Luasnya adalah :' + str(Segiima(sisi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 11:
                    datar(pilihan)
                    sisi = int(input('Masukan Panjang Sisi:'))
                    print('Luasnya adalah :' + str(segienam(sisi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

        case 3:

            operasi(WELCOME)
            # Luas Bangun Datar
            print('Pilihan Operasi :')
            print('1. Keliling Persegi')
            print('2. Keliling Persegi Panjang')
            print('3. Keliling Lingkaran')
            print('4. Keliling Jajar Genjang')
            print('5. Keliling Treapesium')
            print('6. Keliling Layang-Layang')
            print('7. Keliling Belah Ketupat')
            print('8. Keliling Elips')
            print('9. Keliling Segitia')
            print('10. Keliling Segiima')
            print('11. Keliling Segienam')
            print(50*'-')

            pilihan = int(input('Masukan Pilihan : '))

            match pilihan:
                case 1:
                    Keliling(pilihan)
                    sisi = int(input('Masukan Panjang Sisi : '))
                    print('Kelilingnya adalah : ' + str(KPersegi(sisi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 2:
                    Keliling(pilihan)
                    panjang = int(input('Masukan Panjang : '))
                    lebar = int(input('Masukan Lebar : '))
                    print('Kelilingnya adalah : ' +
                          str(KPersegiPanjang(panjang, lebar)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 3:
                    Keliling(pilihan)
                    r = int(input('Masukan Panjang Jari-Jari : '))
                    print('Kelilingnya adalah : ' + str(kLingkarang(r)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 4:
                    Keliling(pilihan)
                    alasA = int(input('Masukan Panjang Alas A : '))
                    alasB = int(input('Masukan Panjang Alas B : '))
                    print('Kelilingnya adalah : ' +
                          str(kJajarGenjang(alasA, alasB)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 5:
                    Keliling(pilihan)
                    sisiA = int(input('Masukan Panjang Sisi A : '))
                    sisiB = int(input('Masukan Panjang Sisi B : '))
                    sisiC = int(input('Masukan Panjang Sisi C : '))
                    sisiD = int(input('Masukan Panjang Sisi D : '))
                    print('Kelilingnya adalah : ' +
                          str(kTrapesium(sisiA, sisiB, sisiC, sisiD)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 6:
                    Keliling(pilihan)
                    sisiBawah = int(input('Masukan Panjang Sisi Atas : '))
                    sisiAtas = int(input('Masukan Panjang Sisi  Bawah : '))
                    print('Kelilingnya adalah : ' +
                          str(kLayang(sisiBawah, sisiAtas)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 7:
                    Keliling(pilihan)
                    sisi = int(input('Masukan Panjang Sisi : '))
                    print('Kelilingnya adalah : ' + str(kBelahKetupat(sisi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 8:
                    Keliling(pilihan)
                    diameter1 = int(input('Masukan Diameter 1 : '))
                    diameter2 = int(input('Masukan Diameter 2 : '))
                    print('Kelilingnya Adalah : ' +
                          str(kElips(diameter1, diameter2)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 9:
                    clear()
                    gambar()
                    print(50*'-')
                    print('SEGITIGA'.center(50, '='))
                    print(50*'-')
                    print('Pilihan Operasi :')
                    print('1. Segitiga Sama Sisi')
                    print('2. Segitiga Sama Kaki')
                    print('3. Segitiga Siku-Siku')
                    print('4. Segitiga Sembarang')
                    print(50*'-')
                    segitiga = int(input('Masukan Pilihan : '))

                    match segitiga:
                        case 1:
                            kSegitiga(segitiga)
                            sisi = int(input('Masukan Panjang Sisi : '))
                            print('Kelilingnya Adalah : ' +
                                  str(kSegitigaSamaSisi(sisi)))

                            pilihanPengulangan = (
                                input('Ingin Mengulangi? (y, n) : '))

                            if pilihanPengulangan == 'y':
                                pengulangan += 1
                            elif pilihanPengulangan == 'n':
                                clear()
                                gambar()
                                print(50*'-')
                                print('terimakasih'.upper().center(50, '='))
                                print(50*'-')

                            else:
                                clear()
                                gambar()
                                print(50*'-')
                                print('tutro baca deks'.upper().center(50, '='))
                                print(50*'-')

                        case 2:
                            kSegitiga(segitiga)
                            sisi = int(input('Masukan Panjang Sisi : '))
                            alas = int(input('Masukan Panjang Alas : '))
                            print('Kelilingnya Adalah : ' +
                                  str(kSegitigaSamaKaki(sisi, alas)))

                            pilihanPengulangan = (
                                input('Ingin Mengulangi? (y, n) : '))

                            if pilihanPengulangan == 'y':
                                pengulangan += 1
                            elif pilihanPengulangan == 'n':
                                clear()
                                gambar()
                                print(50*'-')
                                print('terimakasih'.upper().center(50, '='))
                                print(50*'-')

                            else:
                                clear()
                                gambar()
                                print(50*'-')
                                print('tutro baca deks'.upper().center(50, '='))
                                print(50*'-')

                        case 3:
                            kSegitiga(segitiga)
                            sisi = int(input('Masukan Panjang Sisi : '))
                            alas = int(input('Masukan Panjang Alas : '))
                            print('Kelilingnya Adalah : ' +
                                  str(kSegitigaSiku(alas, sisi)))

                            pilihanPengulangan = (
                                input('Ingin Mengulangi? (y, n) : '))

                            if pilihanPengulangan == 'y':
                                pengulangan += 1
                            elif pilihanPengulangan == 'n':
                                clear()
                                gambar()
                                print(50*'-')
                                print('terimakasih'.upper().center(50, '='))
                                print(50*'-')

                            else:
                                clear()
                                gambar()
                                print(50*'-')
                                print('tutro baca deks'.upper().center(50, '='))
                                print(50*'-')

                        case 4:
                            kSegitiga(segitiga)
                            sisiA = int(input('Masukan Panjang Sisi A : '))
                            sisiB = int(input('Masukan Panjang Sisi B : '))
                            sisic = int(input('Masukan Panjang Sisi C : '))
                            print('Kelilingnya Adalah : ' +
                                  str(kSegitigaSembarang(sisiA, sisiB, sisiC)))

                            pilihanPengulangan = (
                                input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 10:
                    Keliling(pilihan)
                    sisi = int(input('Masukan Panjang Sisi : '))
                    print('Kelilingnya adalah : ' + str(kSegilima(sisi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')

                case 11:
                    Keliling(pilihan)
                    sisi = int(input('Masukan Panjang Sisi : '))
                    print('Kelilingnya adalah : ' + str(kSegienam(sisi)))

                    pilihanPengulangan = (input('Ingin Mengulangi? (y, n) : '))

                    if pilihanPengulangan == 'y':
                        pengulangan += 1
                    elif pilihanPengulangan == 'n':
                        clear()
                        gambar()
                        print(50*'-')
                        print('terimakasih'.upper().center(50, '='))
                        print(50*'-')

                    else:
                        clear()
                        gambar()
                        print(50*'-')
                        print('tutro baca deks'.upper().center(50, '='))
                        print(50*'-')
