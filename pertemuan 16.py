# Latihan untuk Menguji Pemahaman
# Waktunya menjadi master dictionary!

# Latihan 1: Iterasi dan Kalkulasi

# Diberikan dictionary harga buah: harga_buah = {"apel": 5000, "jeruk": 8500, "mangga":
# 7800, "pisang": 3000}.
# Gunakan for loop dan .items() untuk mencetak setiap buah dan harganya dalam format "Harga 1 kg
# [nama buah] adalah Rp [harga]". Di akhir, hitung dan cetak total harga semua buah.

harga_buah = {"apel": 5000, "jeruk": 8500, "mangga": 7800, "pisang": 3000}
total = 0
for buah, harga in harga_buah.items():
    print(f"Harga 1 kg {buah} adalah Rp {harga}")
    total += harga
print("Jadi, semuanya Rp.",total)

# Latihan 2: Manajemen Kontak

# Buat program manajemen kontak sederhana:
# -. Buat dictionary kosong bernama kontak.
# /. Tambahkan tiga kontak (misal: "Ibu", "Ayah", "Teman") beserta nomor teleponnya.
# 0. Ubah nomor telepon "Ibu".
# 1. Gunakan .pop() untuk menghapus "Teman".
# 3. Cetak dictionary kontak akhir.

kontak = {}
kontak["Ibu"] = "62811111111"
kontak["Ayah"] = "62822222222"
kontak["Teman"] = "62833333333"

kontak["Ibu"] = "628000000"
kontak.pop("Teman")
print(kontak)

# Latihan 3: Nested Dictionary

# Buatlah sebuah nested dictionary untuk menyimpan data dua produk di sebuah toko online.
# Key utamanya adalah ID produk (misal: "PROD001", "PROD002").
# Setiap produk harus memiliki key untuk "nama", "harga", dan "stok".
# Setelah membuatnya, tulis kode untuk mencetak nama dan harga dari produk dengan ID "PROD002".

produk = {
    "PROD001": {"nama": "Laptop", "harga": 8500000, "stok": 10},
    "PROD002": {"nama": "HP", "harga": 3500000, "stok": 25}
}
print("Nama & harga PROD002:", produk["PROD002"]["nama"], produk["PROD002"]["harga"])

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
