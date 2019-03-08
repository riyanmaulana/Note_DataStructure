# ASD Project Meet 3 - (Infix, Postfix, Prefix)
# Creator={Riyan Maulana - 170411100065}

# Infix, Postfix, Prefix

# Infix adalah cara penulisan atau ungkapan yang meletakan operator di tengah antara 2 operand dalam hal ini dalam kurung sangat menentukan posisi.
# Contoh Infix :
# A + B
# ( A - B ) * C

# Prefix adalah cara penulisan atau ungkapan yang meletakan operator disebelah kiri 2 operand dan dalam kurung sangat menentukan posisi.
# Contoh Prefix :
# + A B
# * - A B C

# Posfix adalah cara penulisan yang meletakan operator disebelah kanan 2 operand dan posisi operand yang berada di dalam kurung sangat menentukan.
# Contoh Postfix :
# A B +
# A B - C *


#Algoritma infix ke postfix
# berikut untuk konversi ekspresi aritmatik infix ke postfix

# 1. Buat struktur data stack untuk menampung operator
# 2. Baca ekspresi aritmatik dari kiri ke kanan tiap token
    # jika token yang dibaca adalah kurung buka maka push kurung buka tersebut kedalam stack
    # jika token yang dibaca adalah kurung tutup maka pop stack semua token sampai ditemukan kurung buka
    # jika token yang dibaca adalah operator maka
        # - pop operator yang memiliki tingkat lebih tinggi atau sama dan masukkan operator tsb kedalam output string.
        # - push token operator kedalam stack
# 3. jika masih terdapat operator pada stack, maka operator yang tersisa dan letakkan pada output string  


# Example Syntax : (Coming soon/Menyusul)

# (Karena masih belum dijelaskan secara langsung kedalam program)