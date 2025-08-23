# Latihan 1: Membuat dan Mengakses
# -. Buatlah sebuah list bernama jadwal_senin yang berisi nama-nama mata pelajaran hari Senin:
# "Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah".
# /. Cetak seluruh list. 
# . Cetak hanya mata pelajaran pertama.
# 1. Cetak mata pelajaran terakhir menggunakan indeks negatif.
jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]

print(jadwal_senin)       # Cetak semua
print(jadwal_senin[0])    # Mata pelajaran pertama
print(jadwal_senin[-1])   # Mata pelajaran terakhir

# Latihan 2: Modifikasi List
# -. Gunakan list jadwal_senin dari latihan sebelumnya.
# /. Ternyata jam pelajaran "Olahraga" dipindah ke hari Selasa. Ubah elemen "Olahraga" menjadi
# "Kimia".
# 0. Cetak list jadwal_senin yang sudah diperbarui.
# Gunakan list dari latihan sebelumnya
jadwal_senin[2] = "Kimia"
print(jadwal_senin)
