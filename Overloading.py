
# coding: utf-8

# Overloading

# 08 Oktober 2018

# => operator overloading adalah pembuatan beberapa fungsi atau kegunaan untuk suatu operator. Misalnya operator + dibuat tidak hanya untuk penjumlahan, tapi juga untuk fungsi lain <br/>
# => method overloading adalah fungsi yang memiliki nama yang sama di dalam kelas, tapi dengan jumlah dan tipe argumen yang berbeda sehingga dapat melakukan beberapa hal yang berbeda <br/>
#   hal-hal yang perlu diperhatikan dalam method overloading:
#    - jumlah parameterya berbeda
#    - tipe data parameternya berbeda

'''
mendefinisikan dua metode produk,
tapi kita hanya bisa menggunakan metode produk kedua,

karena python tidak mendukung method overloading.

Kami dapat mendefinisikan banyak metode dengan nama yang sama dan argumen yang berbeda tetapi
kami hanya dapat menggunakan metode terbaru yang ditentukan.

Memanggil metode lain akan menghasilkan kesalahan.
'''

#contoh
def add(a,b):
    return a+b
def add(a,b,c):
    return a+b+c
print(add(2,3)) # TypeError: add() missing 1 required positional argument: ‘c’


# Definisi
# - Tentukan metode dengan banyak cara untuk memanggilnya.
# - Dengan metode atau fungsi tunggal, kita dapat menentukan jumlah parameternya sendiri. Tergantung pada definisi fungsi, itu bisa disebut dengan nol, satu, dua atau lebih parameter.


#contoh method overloading
def add(datatype, *args):
    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = ''
        
    for x in args:
        answer = answer+x
    print(answer)
    
#integer
add('int',5,6)

#string
add('str','Hi','Geeks')


class Human:
    def sayHello(self,name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello')
            
#Create instance
obj = Human()

#call the method
obj.sayHello()

#call the method with a parameter
obj.sayHello("Guido")


# Operator Overloading
# 
# Operator Overloadinf dapat memungkinkan untuk menjabarkan atau mendefinisikan kembali operator '+' Operator -> untuk menambahkan kedua bilangan atau objek bisa berupa 'int' maupun 'str'.<br/>
# Operator overloading biasanya mendefinisikan special method atau operator, dicapai dengan mendefinisikan metode khusus dalam definisi kelas


#Operator Overloading
'''
contoh Operator Overloading :
Operator = Method
+  = obejct.__add__(self,other)
-  = object.__sub__(self,other)
*  = object.__mul__(self,other)
// = object.__floordiv__(self,other)
/  = object.__div__(self,other)
%  = object.__mod__(self,other)
** = object.__pow__(self,other)
<  = object.__it__(self,other)
<=  = object.__le__(self,other)
==  = object.__eq__(self,other)
!=  = object.__ne__(self,other)
>=  = object.__ge__(self,other)
dan masih banyak lagi, bisa dilihat di dalam ppt overloading
'''

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        
    def show(self):
        print(self.num + "/" + self.den)
        
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
    
    def __mul__(self,otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return (newnum,newden)

f1 = Fraction(1,4)
f2 = Fraction(1,2)
print(f1+f2) #bisa juga denga menulis (f1.__add__(f2))
print(f1*f2)

class Perkalian:
    def __init__(self,angka1,angka2):
        self.num = angka1
        if len(str(angka2)) > 1:
            for i in range(len(str(angka2))):
                angka2 *= 0.1
        self.den = angka2
        
    def __str__(self):
        return str(self.num) + "." + str(self.den)
        
    def __mul__(self,otherfraction): #perkalian koma-koma
        newnum = (self.num + self.den) * otherfraction.den
        newden = otherfraction.num * (self.num + self.den)
        print(newnum + newden)

p1 = Perkalian(1,2)
p2 = Perkalian(2,32)
p1*p2



#Kelas koordinat
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    #kedua __str__ sama saja, cuma cara penulisannya saja yang beda
#    def __str__(self):
#        return "({0},{1})".format(self.x,self.y)
    def __str__(self):
        return "Point object is at: (" + str(self.x) + "," + str(self.y) + ")"
    
    def __add__(self,other):
        x = self.x - other.x
        y = self.y - other.y        
        return Point(x,y)
    
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        jarak = x**2 + y**2
        return (jarak)

p1 = Point(1,3)
p2 = Point(-1,2)
print(p1+p2) #atau p1.__add__(p2)
print(p1-p2)

