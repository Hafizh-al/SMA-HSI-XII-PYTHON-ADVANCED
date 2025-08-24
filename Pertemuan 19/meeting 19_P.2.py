# Latihan 2: Validasi Nomor Telepon Sederhana

# Buat program yang meminta pengguna memasukkan nomor telepon. Program harus memvalidasi apakah
# input tersebut hanya berisi angka dan panjangnya antara 10 sampai 13 digit.
# Gunakan re.search() dengan jangkar ^ dan $.
# Gunakan quantifier + atau yang lebih spesifik.
# Cetak "Format nomor telepon valid." atau "Format tidak valid."
# Pola yang mungkin: ^\d+$ (ini hanya mengecek apakah semuanya digit, kamu perlu menambahkan
# pengecekan panjang dengan len()).

print("-----Latihan 2-----")
import re

nomor = input("Masukkan nomer telpon: ")
if re.search(r'^\d+$', nomor) and 10 <= len(nomor) <= 13:
    print("Format nomor telpon valid.")
else:
    print("Format tidak valid.")    
