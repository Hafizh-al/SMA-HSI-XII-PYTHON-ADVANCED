# Latihan 1: Sintaks Tuple
# -. Buatlah sebuah tuple bernama hari yang berisi nama-nama hari dari Senin sampai Minggu.
# /. Buatlah sebuah tuple bernama angka_ganjil yang hanya berisi satu angka: 7. Pastikan tipenya
# benar-benar tuple.
# 0. Cetak kedua tuple dan tipe datanya.

print("-----Latihan 1-----")
hari = ("Ahad", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu")
angka_ganjil = (7,)
print(hari)
print(type(hari))
print(angka_ganjil)
print(type(angka_ganjil))

# Latihan 2: Immutability
# Diberikan tuple koordinat_awal = (10, 20). Tulis kode yang menghasilkan tuple baru bernama
# koordinat_baru yang nilainya (10, 25). Kamu tidak boleh mengubah koordinat_awal secara
# langsung.

print("_____Latihan 2_____")
tuple_koordinat_awal = (10, 20)
koordinat_baru = (tuple_koordinat_awal[0], 25)

print("Koordinat awal:", tuple_koordinat_awal)
print("Koordinat baru:", koordinat_baru)

# Latihan 3: Tuple Assignment
# Sebuah fungsi mengembalikan informasi RGB sebuah warna sebagai tuple: warna = (255, 165, 0).
# Gunakan tuple assignment untuk "membongkar" nilai tersebut ke dalam tiga variabel terpisah: red, green,
# dan blue. Cetak ketiga variabel tersebut.

print("_____Latihan 3_____")
warna = (255, 165, 0)
red, green, blue = warna

print("Red:", red)
print("Green:", green)
print("Blue:", blue)

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