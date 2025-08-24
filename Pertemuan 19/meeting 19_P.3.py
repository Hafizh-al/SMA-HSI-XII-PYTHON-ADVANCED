# Latihan 3: re.search() vs. re.findall()

# Diberikan string teks = "python adalah bahasa yang menyenangkan, python mudah
# dipelajari.".
# -. Gunakan re.search('python', teks). Apa yang dikembalikannya? Cetak .group()-nya.
# /. Gunakan re.findall('python', teks). Apa yang dikembalikannya? Cetak hasilnya.
# 0. Jelaskan perbedaan output keduanya.

print("-----Latihan 3-----")
import re
teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."

# search()
hasil_search = re.search('python', teks)
print("Hasil search:", hasil_search.group())

# findall()
hasil_findall = re.findall('python', teks)
print("Hasil findall:", hasil_findall)
