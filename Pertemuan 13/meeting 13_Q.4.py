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
