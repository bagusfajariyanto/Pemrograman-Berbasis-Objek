
# coding: utf-8

# Encapsulation

# 15 Oktober 2018

# Encapsulation => informasi yang disembunyikan dari luar kelas atau biasa disebut private (method dan property), disini encapsulation merupakan suatu cara agar bisa mengakses informasi yang di sembunyikan dari luar kelas dan menjadikannya public
# 
# Akses Public, menandakan komponen tersebut diperbolehkan untuk diakses dari class yang berbeda atau dapat diakses dari luar class
# Akses Private, berarti komponen yang hanya bisa diakses dalam class yang sama.
# 
# - Properti Private adalah properti yang dimiliki oleh sebuah class dan tidak bisa di akses di luar class
# - Method Private adalah sebuah fungsi di dalam sebuah class dan tidak bisa di akses atau di ambil oleh class lain
# 
# ciri - ciri method private atau ada tanda single( _ ) atau double( __ ) 
# cara akses private:
# - untuk attribut class, namaclass()._namaClass_namaAttribut
# - untuk method class, namaclass()._namaClass_namaMethod


class A(object):
    # public method
    def myPublicMethod(self):
        return "Ini adalah Public method"

    # private method with single _underscore
    def _myPrivateMethod(self):
        return "Ini adalah Private method"

    # private metod with double __undersore
    def __myAnotherPrivateMethod(self):
        return "Ini adalah Private Method yang lain"


obj = A()
# Kita bisa mengakses public method yang keren !!!
print(obj.myPublicMethod())   #Output : Ini adalah Public Mehod

# Perhatikan bahwa kami juga dapat mengakses metode pribadi dari luar
print(obj._myPrivateMethod()) #Output : Ini adalah Private method

# Namun, Anda masih bisa memanggil method double underscore ( __ )
# dengan menambahkan nama _class sebelum nama metode
print(obj._A__myAnotherPrivateMethod()) #Output: Ini adalah Private Method yang lain



#contoh
class Robot(object):
    def __init__(self):
        self._version = 22
        
    def getVersion(self):
        print(self._version)
        
    def setVersion(self,version):
        self._version = version

obj = Robot()
obj.getVersion()
obj.setVersion(12)
obj.getVersion()
print(obj._version)
#print(obj._Robot_version)


class Car:
    
    __maxspeed = 0
    __name = ""
    
    def __inti__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
        
    def drive(self):
        print("Diving, maxspeed " + str(self.__maxspeed))
        
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
        
redcar = Car()
redcar.drive()
redcar.setMaxSpeed(10)
redcar.drive()


class Car:
    def __init__(self):
        self.__updateSoftware()
        
    def drive(self):
        print('diving')
        
    def __updateSoftware(self,software):
        print('updating software')
        
redcar = Car()
redcar.drive()
redcar._Car__updateSoftware()


#Contoh lain
class Persegi:    
    def __init__(self):
        self.__sisi = 5
    def tampilkansisi(self):
        print("Sisi =",self.__sisi)
    def luas(self):
        print("Luas =",self.__sisi ** 2)
    def __setSisi(self,newsisi):
        self.__sisi = newsisi

print("Persegi")
p = Persegi()
p.tampilkansisi()
p.luas()
p._Persegi__setSisi(9) #memanggil method private secara langsung
print(p._Persegi__sisi) #memanggil attribute private secara langsung
p.luas()

class Persegi_panjang():
    def __init__(self):
        self.si= p._Persegi__sisi
        self.lebar = 8
        
    def luas(self):
        print("Luas Persegi Panjang = ",self.si * self.lebar)
        
    def setPanjang(self,panjang,lebar):
        self.si = panjang
        self.lebar = lebar
        
print("Persegi Panjang")
pp = Persegi_panjang()
pp.luas()
pp.setPanjang(10,4)
pp.luas()

