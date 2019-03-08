# ASD Project Meet 1 - (Review)
# Creator={Riyan Maulana - 170411100065}

# Program ini merupakan catatan untuk mempelajari review Algoritma, ada beberapa program yang tidak bekerja dengan sempurna.. Ini merupakan sample

# -------- > Algoritma Sequence - Konversi Kurs Mata Dollar ke Rupiah
dollar = int(input("Jumlah Dollar : "))
rupiah = dollar*15000
print(dollar, "$ = Rp. ", rupiah)


# -------- > Algoritma Branching - Penentuan jenis bilangan
num = int(input("Masukkan bilangan = "))
if num %2==0:
    print(num, "Merupakan bil.genap")
else:
    print(num, "Adalah bilangan ganjil")


# Alg-------- > oritma Iteration - Menampilkan sejumlah n bilangan genap
num = int(input("BIl. genap : "))
count = 1
i = 0
while count<=num:
    if i %2==0:
        print(count, '. ', i)
        count = count + 1
    i = i + 1

n = int(input("Bil. genap : "))
count = 10
i = 0
while i < count:
    if i %2==1:
        print(i, "Bil. genap")
    i = i+1


# -------- > Algoritma Iteration - Menampilkan factorial suatu bilangan
def faktorial():
    x = int(input("Masukkan angka : "))
    faktorial = 1
    for i in range(1, x+1):
        print(i)
        faktorial = faktorial*i
    print("Faktorial dar x", x, "adalah ", faktorial)
faktorial()

x = int(input("Masukkan angka : "))
fak = 1
for y in range(1, x+1):
    # print(x)
    fak = fak*x
print("Faktorial dari x", x, " adalah ", fak)


# Tipe data String dan offset
# Contoh inisialisasi variabel dengan tipe data string, dan cara pengaksesan satu dan lebih dari satu karakter.
# Elemen atau anggota pada String bersifat Immutable atau tidak dapat dirubah dengan melalui operasi assignment.
# Akan tetapi nilai string dapat dirubah melalui method replace yang terdapat pada string

data = "Where is waldo?"
# print(len(data))
print(data[12]) #satu karakter
temp = data[9:14]   #lima karakter
print(temp)


# Berikut contoh code untuk proses perubahan nilai melalui operasi assignment, dan melalui method pada string
# immutable, tidak dapat dirubah melalui assignment operator

data = "Where is waldo?"
# data[13]="i"
print(data)
# Maka error, karena tidak dapat dirubah

# nilai dirubah melalui method 'replace'
# data = "Where is Waldo?"
# data.replace("o","i")
# print(data)
# This program is not working

# -------- > List
#     adalah struktur data yang terdiri dari beberapa elemen atau anggota list dengan berbagai tipe data.
arrData = [1, 2, "Python", 0.8, "numpy"]
print(arrData)
print(arrData[1])
print(arrData[1:4])

# # Berikut adalah contoh code untuk merubah nilai elemen dari suatu list

arrData = [1, 2, "Python", 0.8, "numpy"]
print(arrData)
arrData[2]="Java"
print(arrData)

# # List 2D
# #   adalah list yang berbentuk dua dimensi, yaitu bentuk data seperti halnya matriks dua dimensi, yang memiliki baris dan kolom (List dalam list).

arr2 = [[1,2,3], [4,5,6]]
print(arr2)
print(arr2[1][2])


# -------- > Tuple
# sama halnya dengan list, tuple ini terdiri dari beberapa elemen, dan elemen tersebut dapat terdiri dari berbagai tipe.
# Cara pengaksesan elemen atau anggotanya, dilakukan dengan menuliskan index tuple.

tupData = (1,2,"Python", 0.8, "numpy")
print(tupData)
print(tupData[2])
print(tupData[1:3])

# Elemen pada tuple bersifat immutable, nilai anggota tidak dapat dirubah.
# Oleh karena itu tuple biasanya digunakan untuk merepresentasikan kumpulan data konstan, dan untuk index dictionary (karena index tidak boleh dirubah).

tupData = (1,2,"Python", 0.8, "numpy")
print(tupData)
print(tupData[2])
# tupData[2]="Java"
temp=tupData[4]
# print(tupData)
print(temp)


# -------- > Dictionaries
#   Dictionaries ini hampir sama dengan struktur data List hanya saja, jika pada list menggunakan index berupa integer untuk menunjukkan posisi elemen
# di dalam list, maka pada dictionaries ini, maka index pada dictionaries yang digunakan tidak hanya bertipe integer, akan tetapi string juga dapat 
# digunakan sebagai index. Sehingga untuk keperluan tertentu, dictionaries ini akan lebih cocok digunakan untuk merepresentasikan suatu data. 

# Pada dictionaries, index ini disebut juga dengan keys
# Inisialisasi variabel yang berbentuk dictionaries ini dapat dilakukan dengan dua cara, yaitu

# Menuliskan semua anggotanya secara langsung, namaVariabel={key1:data1, key2:data2,...}
# Menuliskan satu-persatu anggotanya

# example, step 1
sd = {"001":"Ranti","002":"Diana","003":"Budi","004":"Eri"}
print(sd)


# example, step 2
studentData={}
studentData["001"]="Fatimah"
studentData["002"]="Sofia"
studentData["003"]="Ahmad"
studentData["005"]="Ali"
print(studentData)

#   Seperti halnya list, dictionaries juga dapat berbentuk 2D, yaitu elemen-elemen disusun pada baris dan kolom tertentu, 
# sehingga untuk mengakses suatu data, diperlukan dua buah indeks. Karena dibutuhkan dua buah index pada dictionaries ini,
# maka index harus berbentuk tuple (karena sifat index yang tidak boleh dirubah nilainya), sehingga index dictionaries 2D 
# ini ditunjukkan dengan pasangan data atau tuple, '(indeks1,indeks2)'


# Salah satu implementasi Dictionaries ini adalah Sparse Matrix. Sparse Matrix merupaan matrix yang memiliki banyak nilai nol,
# sehingga jika menggunakan list, akan banyak memori yang dibutuhkan.

# Mat = | 0 0 0 0 |
#       | 0 0 0 0 |
#       | 0 2 0 0 |
#       | 0 0 0 3 |
      
# Implementasikan dalam dictionaries
mat = {(0,3):1,(2,1):2,(3,3):3}
mat = {(0,3):1,(2,1):2,(3,3):3}
print(mat)

# Implementasikan dalam list
mat = [[0,0,0,1],[0,0,0,0], [0,2,0,0], [0,0,0,3]]
print(mat,"\n")

# Contoh code pembuatan *sparse matrix * dengan menggunakan dictionary
mat = {(0,3):1,(2,1):2,(3,3):3}
print(mat)
mat[0,2]=4  #penambahan data baru
print(mat)

# Pengecekan data pada index (ind1,ind2), jika tidak terdapat data, maka return value=None, 
#jika terdapat data maka return value=adalah data
cek=mat.get((0,1))
print(cek)
cek=mat.get((2,1))
print("(2,1)=",cek)
cek=mat.get((1,3))
print("(1,3)=",cek)


# -------- > Function¶
#   dengan function maka syntax" pada program dikelompokkan berdasarkan fungsinya masing-masing. Dengan pengelompokan ini,
# maka program akan lebih mudah untuk dibaca maupun diperbaiki.

# Terdapat dua hal penting yang harus diperhatikan, yaitu

# Parameter/argumen : merupakan nilai yang dikirim oleh syntax pemanggil function
# Return Value : merupakan nilai yang dihasilkan oleh function, dan dikirim kembali ke pemanggil function

# Example1 (Without parameters)
def addNumbers():
    a = int(input("Bil. Pertama : "))
    b = int(input("Bil. Kedua : "))
    print("Hasil = ", a + b)

#main program
addNumbers()      #memanggil fungsi addNumbers agar dieksekusi


# Example2 (With parameters)
def addNumber(a,b):
    print("Result = ", a + b)

#main program
num1 = int(input("First num : "))
num2 = int(input("Second num : "))
addNumber(num1, num2)


# Function dengan parameter dan return value
def addNumberss(x,y):
    results = x + y
    return results

def checkGenap(num):
    if num%2==0:
        return True
    else:
        return False

# #Main program
nums1 =int(input("Bilangan pertama = "))
nums2 =int(input("Bilangan kedua = "))
results=addNumberss(nums1,nums2)    #memanggil fungsi agar dieksekusi
if checkGenap(results):
    print(results, " Adalah bilangan genap")
else:
    print(results, "Adalah bilangan ganjil")

# -------- > Module
#   Module ini merupakan suatu file yang terdiri dari sebuah atau lebih dari satu function. 
# Dengan mengelompokkan function-function dalam suatu file, akan memudahkan programmer untuk membaca program dan merubah atau memperbaharui program.

# import filename
# from fileName import *

# Perbedaan kedua perintah import tersebut adalah pemanggilan function yang terdapat di dalam modul.
# Pada pilihan pertama, untuk memanggil fungsi yang ada di modul ini maka menggunakan perintah filename.namaFungsi Sedangkan pada pilihan kedua, 
# untuk memanggil fungsi yang ada di modul ini maka menggunakan perintah namaFungsi

# Berikut contoh pemanggilan module yang sudah dibuat yaitu checkPrime.  Module ini dapat dilihat pada folder code
# import faktorial