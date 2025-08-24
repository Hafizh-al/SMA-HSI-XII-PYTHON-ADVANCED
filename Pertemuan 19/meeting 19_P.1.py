# Latihan untuk Menguji Pemahaman
# Waktunya melatih otot Regex-mu!


# Latihan 1: Temukan Semua Angka

# Diberikan string: data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan
# pengeluaran sebesar Rp 850,000.".
# Gunakan re.findall() untuk mengekstrak semua urutan angka dari string tersebut. Output yang
# diharapkan adalah ['1', '500', '000', '850', '000'].

print("-----Latihan 1-----")
data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan pengeluaran sebesar Rp 850,000."
import re
print(re.findall(r'\d+', data))

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

# Latihan 3: re.search() vs. re.findall()

# Diberikan string teks = "python adalah bahasa yang menyenangkan, python mudah
# dipelajari.".
# -. Gunakan re.search('python', teks). Apa yang dikembalikannya? Cetak .group()-nya.
# /. Gunakan re.findall('python', teks). Apa yang dikembalikannya? Cetak hasilnya.
# 0. Jelaskan perbedaan output keduanya.

print("-----Latihan 3-----")
teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."

# search()
hasil_search = re.search('python', teks)
print("Hasil search:", hasil_search.group())

# findall()
hasil_findall = re.findall('python', teks)
print("Hasil findall:", hasil_findall)

# Latihan 4: Menemukan Kata dengan Pola

# Diberikan kalimat: kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan.".
# Gunakan re.findall() untuk menemukan semua kata yang diakhiri dengan huruf 'g'.

print("-----Latihan 4-----")
kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
import re

kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
hasil = re.findall(r'\w+g', kalimat)
print("Kata yang cocok:", hasil)