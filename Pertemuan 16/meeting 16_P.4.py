# Latihan 4: Frekuensi Hari
# Tulis program yang membaca file mbox-short.txt. Bangun histogram menggunakan dictionary untuk
# menghitung berapa banyak pesan yang dikirim pada setiap hari dalam seminggu. (Lihat baris yang dimulai
# dengan "From ", kata ketiganya adalah hari). Cetak dictionary hasilnya

penghitung_hari = {}
with open("mbox-short.txt") as file:
    for baris in file:
        if baris.startswith("From "):
            kata = baris.split()
            hari = kata[2]
            penghitung_hari[hari] = penghitung_hari.get(hari, 0) + 1

print(penghitung_hari)