print("Calculator Python")
print("-----------------")
print("+ Tambah")
print("- Kurang")
print("* Kali")
print("/ Bagi")
print("-----------------")

#logic
def tambah(x,y):
    return x+y
def kurang(x,y):
    return x-y
def kali(x,y):
    return x*y
def bagi(x,y):
    return x/y

tipe = input("Silakan masukan simbol:")

if tipe in ('+','-','*','/'):
    angka1 = float(input("angka pertama:"))
    angka2 = float(input("angka kedua:"))
    print("-----------------")
    if tipe == "+":
        print("Jumlah:", tambah(angka1, angka2))
    if tipe == "-":
        print("Jumlah:", kurang(angka1, angka2))
    if tipe == "*":
        print("Jumlah:", kali(angka1, angka2))
    if tipe == "/":
        print("Jumlah:", bagi(angka1, angka2))
