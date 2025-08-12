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

# Latihan 3: Traversing dan Modifikasi
# -. Buat sebuah list berisi angka: nilai_mentah = [55, 63, 72, 81, 90].
# /. Buatlah sebuah for loop yang menggunakan range(len(nilai_mentah)) untuk mengunjungi
# setiap elemen.
# 0. Di dalam loop, tambahkan 5 poin ke setiap nilai sebagai "nilai bonus".
# 1. Setelah loop selesai, cetak list nilai_mentah yang sudah berisi nilai-nilai baru.
nilai_mentah = [55, 63, 72, 81, 90]

for i in range(len(nilai_mentah)):
    nilai_mentah[i] += 5  # Tambah bonus 5 poin

print(nilai_mentah)

# Latihan 4: Slicing dan Penggabungan
# -. Buat dua buah list: awal_minggu = ["Senin", "Selasa", "Rabu"] dan akhir_minggu =
# ["Kamis", "Jumat", "Sabtu", "Minggu"].
# /. Gunakan operator + untuk menggabungkan keduanya menjadi list baru bernama seminggu.
# 0. Dari list seminggu, gunakan slicing untuk membuat list baru bernama hari_kerja yang hanya
# berisi hari Senin sampai Jumat.
# 1. Cetak list hari_kerja.
awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]

seminggu = awal_minggu + akhir_minggu
hari_kerja = seminggu[:5]

print(hari_kerja)
