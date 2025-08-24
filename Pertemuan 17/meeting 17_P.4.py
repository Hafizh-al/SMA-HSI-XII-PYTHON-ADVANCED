# Latihan 4: Dictionary dengan Tuple Key
# Buatlah sebuah dictionary bernama papan_catur. Gunakan tuple (baris, kolom) sebagai key
# untuk menyimpan nama bidak catur. Contoh:
# papan_catur[(1, 'a')] = "Benteng Putih"
# papan_catur[(8, 'h')] = "Benteng Hitam"
# Isi beberapa posisi, lalu akses dan cetak bidak yang ada di posisi (1, 'a').

print("-----Latihan 4-----")
# Dictionary dengan tuple sebagai key
papan_catur = {}
papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(7, 'h')] = "Benteng Hitam"
print(papan_catur)
# Akses nilai berdasarkan key tuple
print("Posisi (1, 'a'):", papan_catur[(1, 'a')])
print("Posisi (7, 'h'):", papan_catur[(7, 'h')])