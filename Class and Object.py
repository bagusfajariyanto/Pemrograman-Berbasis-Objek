
# coding: utf-8

# Pemrograman Berbasis Objek

# Class and Object

# September 03 2018

# We can create "things" with:
# - atributes things those "things" have => merupakan barang atau properti yang ada
# - methods things those "things" can do => suatu rancangan yang menggunakan properti dari atributes
# 
# Pengertian Class and Object
# - Class merupakan suatu entitas yang berupa bentuk program yang menjadi sebuah tempat untuk menyimpan data, nilai-nilai dan perilaku (behavior) bersama-sama. Instans dari class merupakan realisasi dari beberapa objek.
# - Object merupakan Instance dari class. Jika class secara umum merepresentasikan (template) sebuah object, maka sebuah instance adalah representasi nyata dari class itu sendiri.
# 
# Perbedaan Class and Object
# - Class = adalah tempatnya atau wadah
# - Object = Instansi dari Class (membuat suatu rancangan dengan menggunakan Class)

# keyword Class diikuti dengan nama Class yang kita inginkan
# lebih baik digunakan kata yang diawali huruf kapital


#contoh class
class Persegi:
    def __init__(self,s): #constructor
        self.sisi = s
    def tampilkansisi(self):
        print("Sisi =",self.sisi)
    def luas(self):
        print("Luas =",self.sisi ** 2)

#main program
kotak = Persegi(4)
kotak.tampilkansisi()
kotak.luas()



# Kubus
class Kubus:
    def __init__(self,s):
        self.sisi = s
    def tampilkansisi(self):
        print("Sisi =",self.sisi)
    def luassisi(self):
        print("Luas Sisi =",self.sisi ** 2)
    def volume(self):
        print("Volume =",self.sisi**3)
    def luaspermukaan(self):
        print("Luas Permukaan =",self.sisi**2 * 6)
    
#mainKubus
kub = Kubus(4)
kub.luassisi()
kub.volume()
kub.luaspermukaan()


# Data Mahasiswa

class Mahasiswa:
    def __init__(self,nim,nama,nilai):
        self.npm = nim
        self.name = nama
        self.ipk = nilai
    def datamahasiswa(self):
        print("NIM :",self.npm)
        print("NAMA :",self.name)
        print("IPK :",self.ipk)
    def predikat(self):
        nil = self.ipk
        print("Hasil Nilai ",end="")
        if nil >= 3.5:
            print("Cumlaud")
        elif 3.5 > nil and nil > 3:
            print("Sangat Memuaskan")
        elif 3 >= nil and nil > 2.5:
            print("Memuaskan")
        elif nil <= 2.5:
            print("Cukup")


mhs = Mahasiswa(11100045,"Bagus",3)
mhs.datamahasiswa()
mhs.predikat()


# ATM Rekening

class Nasabah:
    def __init__(self,nonasabah,nama,norekening):
        self.nonas = nonasabah
        self.name = nama
        self.norek = norekening
    def rekening(self):
        return self.norek
    def isisnya(self):
        print("No Nasabah :",self.nonas)
        print("Nama :",self.name)
        print("No Rekening :",self.norek)
           
class Rekening:
    def __init__(self,saldo,norekening):
        self.saldo = saldo
        self.norek = norekening
    def ceksaldo(self):
        print("Saldo Anda =",self.saldo)
    def setor(self):
        setor = int(input("Masukkan Nominal yang disetor = "))
        self.saldo -= setor
        print("Transfer Uang Berhasil")
        print("Nominal =",setor)
    def ambiluang(self):
        ambil = int(input("Masukkan Nominal yang ingin anda ambil = "))
        self.saldo -= ambil
        print("Uang Berhasil di ambil")       


#main Nasabah and Rekening
nama = str(input("Masukkan Nama = "))
nas = Nasabah(1704111,nama,541120028590)
norek = nas.rekening()

rek = Rekening(15000,norek)
rek.ceksaldo()
rek.setor()
rek.ceksaldo()
rek.ambiluang()
rek.ceksaldo()



# Operasi Bilangan Bulat

class Operasi:
    def __init__(self,bil1,bil2):
        self.bil = bil1
        self.bil2 = bil2
        
    def jumlah(self):
        print("{} + {} = ".format(self.bil,self.bil2),self.bil + self.bil2)
        
    def kurang(self):
        print("{} - {} = ".format(self.bil,self.bil2),self.bil - self.bil2)
        
    def bagi(self):
        print("{} / {} = ".format(self.bil,self.bil2),self.bil / self.bil2)
        
    def kali(self):
        print("{} * {} = ".format(self.bil,self.bil2),self.bil * self.bil2)
        
op = Operasi(12,4)
op.jumlah()
op.kurang()
op.bagi()
op.kali()
