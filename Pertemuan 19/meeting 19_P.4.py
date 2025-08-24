# Latihan 4: Menemukan Kata dengan Pola

# Diberikan kalimat: kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan.".
# Gunakan re.findall() untuk menemukan semua kata yang diakhiri dengan huruf 'g'.

print("-----Latihan 4-----")
kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
import re

kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
hasil = re.findall(r'\w+g', kalimat)
print("Kata yang cocok:", hasil)