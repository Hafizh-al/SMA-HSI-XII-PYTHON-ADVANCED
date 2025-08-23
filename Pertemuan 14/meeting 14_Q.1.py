# Latihan 1: Manajemen Daftar Belanja
# -. Buat sebuah list kosong bernama belanjaan.
# /. Gunakan .append() untuk menambahkan "Telur", "Susu", dan "Roti".
# 0. Gunakan .insert() untuk menambahkan "Apel" di posisi paling awal.
# 1. Gunakan .remove() untuk menghapus "Susu".
# 3. Cetak list akhir.

belanjaan = []
belanjaan.append("Telur")
belanjaan.append("Susu")  
belanjaan.append("Roti")
belanjaan.insert(0, "Apel")
belanjaan.remove("Susu")
print("Si A sudah belanja:", belanjaan)
