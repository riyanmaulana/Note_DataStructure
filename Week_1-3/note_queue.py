# ASD Project Meet 3 - (Queue)
# Creator {Riyan Maulana - 170411100065}

# Queue pada Struktur Data atau antrian adalah sekumpulan data yang mana penambahan elemen hanya bisa dilakukan pada suatu ujung disebut dengan 
# sisibelakang(rear), dan penghapusan(pengambilan elemen) dilakukan lewat ujung lain (disebut dengan sisi depan atau front). 
# Prinsip pemesanan ini kadang-kadang disebut FIFO, masuk pertama keluar pertama.

# Antrian () membuat antrian baru yang kosong. Tidak perlu parameter dan mengembalikan antrian kosong.
# enqueue (item) menambahkan item baru ke bagian belakang antrian. Perlu item dan tidak mengembalikan apa pun.
# dequeue () menghapus item depan dari antrian. Tidak perlu parameter dan mengembalikan item. Antrian dimodifikasi.
# isEmpty () menguji untuk melihat apakah antrian kosong. Tidak perlu parameter dan mengembalikan nilai boolean.
# size () mengembalikan jumlah item dalam antrian. Tidak perlu parameter dan mengembalikan integer.

# Example Syntax :

def queue():
    q=[]                    #membuat lis
    return (q)
def enqueue(q, data):
    q.insert(0,data)        #memasukkan data secara manual (depan(index), value)
    return (q)              #return q
def dequeu(q):
    data = q.pop()          #pop from front
    return(data)            #return data
def isEmpty(q):
    return(q==[])           #checking if value is null
def size(q):
    return (len(q))         #checking value length value

qt = queue()
enqueue(qt, "cow")          #insert data from front
enqueue(qt, "w")
enqueue(qt, "cat")
print(qt)
print(size(qt))             #count size
dequeu(qt)                  #dequeu / out from front
print(qt)
