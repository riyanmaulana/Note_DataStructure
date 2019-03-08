# ASD Project Meet 2 - (Stack)
# Creator={Riyan Maulana - 170411100065}

# Stack: kumpulan item yang dipesan di mana penambahan item baru dan penghapusan item yang sudah ada selalu terjadi di ujung yang sama. Ujung ini biasanya 
# disebut sebagai "atas." Ujung yang berlawanan atas dikenal sebagai "basis." Prinsip pemesanan ini kadang-kadang disebut LIFO / FILO.

# Stack() membuat tumpukan baru yang kosong. Tidak memerlukan parameter dan mengembalikan tumpukan kosong.
# push(item) menambahkan item baru ke bagian atas tumpukan. Perlu item dan tidak mengembalikan apa pun.
# pop() menghapus item teratas dari tumpukan. Tidak perlu parameter dan mengembalikan item. Tumpukan dimodifikasi.
# peek() mengembalikan item teratas dari tumpukan tetapi tidak menghapusnya. Tidak perlu parameter. Tumpukan tidak diubah.
# isEmpty() menguji untuk melihat apakah tumpukan kosong. Tidak perlu parameter dan mengembalikan nilai boolean.
# size() mengembalikan jumlah item pada stack. Tidak perlu parameter dan mengembalikan integer.



# Example Syntax :

# Step 1
def stack():
    s = []
    return(s)
def push(s, data):
    s.append(data)
def pop(s):
    data = s.pop()
    return (data)
def peek(s):    
    # return items[len(self.items)-1]
    return s[len(s)-1]
    # return len(s[len(s-1)])
def isEmpty():
    return (s==[])
def size():
    return len(s)

# reverse word (membalik kata)
print("Program reverse word : ")
st = stack()                        #Buat variabel untuk memanggil stack
push(st,"R")                        #push data from front 
push(st,"I")
push(st,"Y")
push(st,"A")
push(st,"N")
# pop(st)                           
hasil = ""                          #Buat dan tampung data kedalam var
for x in range(len(st)):            #Loop sebanyak panjang data yang di masukkan 
    hasil = hasil + pop(st)         #tampung nilai dan tambahkan nilai yang di pop tadi secara looping
print(hasil)                        #show result


print("\nImplementasi using stack : ")
st1= stack()                        #Buat variabel untuk memanggil stack
push(st1,100)                       #push data from front 
push(st1,23)
push(st1,34)
# pop(st1)
print(peek(st1))                    #peek(ambil/lihat dari posisi belakang) 
print(st1)

peek(st1)
print(st1)
# push(st1,56)
# print(st1)

print()
# Step 2 : Use class
class Stack ():
    def __init__(self):
        self.items=[]               #make items in constructor (instance)
    def push (self,item):
        self.items.append(item)     
    def pop (self):
        return self.items.pop()
    def size(self):
        return len(self.items)
s1= Stack()
decNum= int(input("Enter the decimal num : "))  
while decNum!=0:                    #loop during not null
    newNum= decNum%2                #gunakan operator modulo dan simpan value di var baru 
    decNum = decNum//2              #bagi pembulatan dengan value
    s1.push(newNum)                 #push data
while s1.size() != 0:               #loop during not null
    a=s1.pop()                      #pop semua item sampai 0, dan simpan valuenya dalam var baru
    print(a, end="")                #show result, and using end = " " for space               
print("")