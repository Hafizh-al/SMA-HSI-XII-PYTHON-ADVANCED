# Latihan 1: Membuat dan Mengakses
# -. Buat sebuah dictionary bernama biodata untuk merepresentasikan dirimu. Isinya harus memiliki
# key: "nama", "umur", "hobi" (hobi bisa berupa list dari beberapa string), dan
# "sudah_menikah" (berisi boolean).
# /. Cetak seluruh dictionary.
# 0. Cetak hanya value dari key "nama".
# 1. Cetak hobi pertamamu dari list hobi.
biodata = {
    "nama": "Muhammad Daffa Al Hafizh",
    "umur": 17,
    "hobi": ["Membaca", "Coding", "Olahraga", "Traveling", "Watching", "etc"],
    "sudah_menikah": False
}
print(biodata)                # Cetak semua
print(biodata["nama"])        # Ambil nama
print(biodata["hobi"][0])     # Ambil hobi pertama
