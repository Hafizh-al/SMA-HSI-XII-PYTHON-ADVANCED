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
