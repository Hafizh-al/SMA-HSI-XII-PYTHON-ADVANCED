# Latihan 3: Analisis Kata
# Buat program yang:
# -. Meminta pengguna memasukkan sebuah kalimat.
# /. Gunakan .split() untuk mengubah kalimat tersebut menjadi sebuah list kata-kata.
# 0. Gunakan len() untuk menghitung dan mencetak jumlah kata dalam kalimat.
# 1. Gunakan .sort() pada list tersebut untuk mengurutkan kata-kata berdasarkan abjad, lalu cetak
# list yang sudah terurut.
 
kalimat = input("Masukin sebuah kalimat: ")
kata_list = kalimat.split()  
print(f"Jumlah kata: {len(kata_list)}")
kata_list.sort() # Urutan sesuai abjad
print("Kata yang urut:", kata_list)
