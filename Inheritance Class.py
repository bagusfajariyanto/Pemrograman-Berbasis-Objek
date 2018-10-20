
# coding: utf-8

# # Inheritance Class

# ### 10 September 2018

# Inheritance => merupakan sebuah kelas dimana kelas tersebut ketika menggunakan kode yang diambil atau disalin ke dalam kelas lain. Kita bisa analogikan inherit ini seperti orang tua dan anak, dimana anak dapat mewarisi gen atau sifat-sifat tertentu yang ada pada orang tua mereka. Contoh, seperti seorang anak yang mewarisi kulit atau hidung orang tua mereka.

# In[ ]:


class User:
    def __init__(self,nama):
        self.name = nama
        
    def printname(self):
        print("Name = ", self.name)

class Programmer(User): #inheritance super class
    def __init__(self,nama,lastname):
        self.lastname = lastname
        super().__init__(nama)
    
    def printlastname(self):
        print("Last Name = " + self.lastname)
        
    def doPython(self):
        print("Programming Python")
               
class Programmer1(User):
    pass
#semua yang ada di user bisa kita ambil tanpa melakukan apapun dan mengambil semua method yang ada di User

brianto = User("Brian")
brianto.printname()

diand1 = Programmer("Diana","sulistiawati")
diand1.printname()

diand = Programmer("Diana","sulistiawati")
diand.printlastname()
diand.doPython()
diand.printname()


# In[ ]:


class Fish:
    def __init__(self,first_name,last_name="Fish",skeleton="bone",eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    
    def swim(self):
        print("The fish is swimming.")
        
    def swim_backwards(self):
        print("The fish can swim backwards.")

class Trout(Fish):
    pass

class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")

terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()
print()

terry1 = Trout("Terrys","SmallFish","no bone",True)
print(terry1.first_name + " " + terry.last_name)
print(terry1.skeleton)
print(terry1.eyelids)
print()

casey = Clownfish("Casey")
print(casey.first_name + " " + terry.last_name)
casey.swim()
casey.live_with_anemone()


# ## Type Inheritance

# TYPE of Inheritance Class
# 
# - default => Semuanya sama dari properti maupun method
# - Overriding => mengubah attribute dari induk, attributenya harus sama persis
# - Super => Mengambil dan menambah attribute yang unix yang di dapat dari induk dan spesifix tidak ada di subclass
# - Multiple => mengambil attribute and method lebih dari siji

# In[ ]:


#Contoh Overriding
class Fish:
    def __init__(self,first_name,last_name="Fish",skeleton="bone",eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    
    def swim(self):
        print("The fish is swimming.")
        
    def swim_backwards(self):
        print("The fish can swim backwards.")
        
class Shark(Fish):
    def __init__(self,first_name,last_name="Shark",skeleton="cartilage",eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim_backwards(self):
        print("The shark cannot backwards, but can sink backwards")


# In[ ]:


class Persegi:
    def __init__(self,sisi,bentuk="Persegi"):
        self.sisi = sisi
        self.bentuk = bentuk
    def display(self):
        print("Sisi:",self.sisi)
        print("Bentuk:",self.bentuk)
    def deskripsi(self):
        print("Deskripsi => bentuk %s dengan jumlah sisi %d, semua sisinya sama panjang"%(self.bentuk,self.sisi))
        
class Persegi_panjang(Persegi):
    def __init__(self,sisi,bentuk="Persegi Panjang"):
        self.sisi = sisi
        self.bentuk = bentuk

    def deskripsi(self):
        print("Deskripsi => bentuk %s dengan jumlah sisi %d, memiliki 2 sisi yang sama panjang"%(self.bentuk,self.sisi))

class Segitiga(Persegi):
    def __init__(self,sisi,bentuk="Segitiga"):
        self.sisi = sisi
        self.bentuk = bentuk

    def deskripsi(self):
        print("Deskripsi => bentuk %s dengan jumlah sisi %d, memiliki 3 sisi yang sama tidak sama panjang"%(self.bentuk,self.sisi))

class Bujur_sangkar(Persegi):
    def __init__(self,sisi,bentuk="Bujur Sangkar"):
        self.sisi = sisi
        self.bentuk = bentuk
        
    def deskripsi(self):
        print("Deskripsi => bentuk %s dengan jumlah sisi %d, memiliki 2 sisi yang sama panjang dan 2 sisi yang sama-sama miring :/"%(self.bentuk,self.sisi))


per = Persegi(4,"Persegi")
per.display()
per.deskripsi()
perpan = Persegi_panjang(4,"Persegi Panjang")
perpan.display()
perpan.deskripsi()
busang = Bujur_sangkar(4,"Bujur sangkar")
busang.display()
busang.deskripsi()
seg = Segitiga(3,"Segitiga")
seg.display()
seg.deskripsi()


# In[ ]:


#contoh Super
class Fish:
    def __init__(self,first_name,last_name="Fish",skeleton="bone",eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    
    def swim(self):
        print("The fish is swimming.")
        
    def swim_backwards(self):
        print("The fish can swim backwards.")
        
class Truot(Fish):
    def __init__(self,water="freshwater"):
        self.water = water
        super().__init__()
        Fish.__init__(self)


# In[ ]:


#contoh Multiple
class Person:
    def __init__(self):
        self.name = input("Nama: ")
        
    def display(self):
        print("Name: ",self.name)
        
class Marks:
    def __init__(self):
        self.npm = input("npm: ")
        print("Nilai")
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        
    def display(self):
        print("NPM: ",self.npm)
        print("Nilai:",self.math,self.biology)
        
class Student(Person,Marks):
    def __init__(self):
        Person.__init__(self)
        Marks.__init__(self)
        
    def result(self):
        Person.display(self)
        Marks.display(self)


stud1 = Student()
stud2 = Student()
stud1.result()
stud2.result()

