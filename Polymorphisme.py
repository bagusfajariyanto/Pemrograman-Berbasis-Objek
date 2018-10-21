
# coding: utf-8

# Review and Polymorphisme

# 1 Oktober 2018

#  - Object adalah Instance dari sebuah class yang sudah kita beri propertinya, masing-masing class memiliki standart yang berbeda-beda, konsep utama dari oop adalah object dan class
#  - polymorphisme terbagi dari kata-kata (poly) yang artinya banyak dan (morphisme) artinya bentuk. Jadi suatu objek yang memiliki banyak bentuk , punya nama yang sama tapi tidak pasti memiliki hasil yang sama. Method di masing-masing kelas memiliki nama yang sama dengan hasil yang berbeda.
#  
# 
# Terkadang suatu objek datang dalam banyak tipe atau bentuk. Jika kita memiliki tombol, ada banyak hasil imbang yang berbeda (tombol bulat, tombol cek, tombol persegi, tombol dengan gambar) tetapi mereka berbagi logika yang sama: onClick (). Kami mengaksesnya menggunakan metode yang sama.
# Ide ini disebut Polymorphism


class Shark():
    def swim(self):
        print("The shark is swimming")
    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards")
    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")

class Clownfish():
    def swim(self):
        print("The clownfish is swimming")
    def swim_backwards(self):
        print("The clownfish can swim backwards.")
    def skeleton(self):
        print("The clownfish's skeleton is made of bone")
        

#With Function
print(1)
def in_the_pasific(fish):
    fish.swim()
    
sammy = Shark()
casey = Clownfish()

in_the_pasific(sammy)
in_the_pasific(casey)

#With Methods
print(2)
sammy = Shark()
casey = Clownfish()

for fish in (sammy,casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton

print(3)
sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()


# Abstact Class
# 


class Document: #abstract class
    def __init__(self,nama):
        self.nama = nama
        
    def show(self):
        raise NotlemplementedError("Subclass must implement abstract method")
        
class pdf(Document):
    def show(self):
        return 'Show pdf contents!'


# Tugas

class Pegawai:
    def __init__(self,nama):
        self.nama = nama
        self.gaj = 3000000
                
    def gaji(self):
        raise NotlemplementedError("Subclass must implement abstract method")
    
class Manajer(Pegawai):
    def __init__(self,nama,tunjangan):
        Pegawai.__init__(self,nama)
        self.tunj = tunjangan
        
    def gaji(self):
        gaji_now = self.gaj + self.tunj
        print("{} mendapatkan gaji total {}".format(self.nama,gaji_now))
        
class Programmer(Pegawai):
    def __init__(self,nama,bonus):
        Pegawai.__init__(self,nama)
        self.bonus = bonus
        
    def gaji(self):
        gaji_now = int(self.gaj) + int(self.bonus)
        print("{} mendapatkan gaji total {}".format(self.nama,gaji_now))
        

abang = Manajer("Bagus Fajariyanto",750000)
adik = Programmer("Fajar Islami",500000)

#Polymorphisme dengan function
def showing(endut):
    endut.gaji()

showing(abang)
showing(adik)

print()

#Polymorphisme dengan method
abang.gaji()
adik.gaji()

