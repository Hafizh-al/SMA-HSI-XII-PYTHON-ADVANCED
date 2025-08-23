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
# Latihan 2: Modiikasi Dictionary
# -. Gunakan dictionary biodata dari Latihan 1.
# /. Tambahkan pasangan key-value baru: "kota": "Nama Kotamu".
# 0. Ubah value dari key "umur" menjadi umurmu tahun depan.
# 1. Cetak dictionary yang sudah diperbarui.
biodata = {
    "nama": "Muhammad Daffa Al Hafizh",
    "umur_tahun_depan": 18,
    "hobi": ["Membaca", "Coding", "Olahraga", "Traveling", "Watching", "etc"],
    "sudah_menikah": False,
    "kota": "Purwokerto"
}
print(biodata) # dictionary yang sudah diperbarui.
# Latihan 3: Penggunaan .get()
# -. Masih dengan dictionary biodata.
# /. Coba akses key "pekerjaan" menggunakan bracket notation []. Apa yang terjadi? (Beri komentar
# pada baris ini agar tidak error).
# 0. Sekarang, akses key "pekerjaan" menggunakan metode .get(). Cetak hasilnya.
# 1. Akses lagi key "pekerjaan" menggunakan .get(), tapi kali ini berikan nilai default "Pelajar".
# Cetak hasilnya.
# print(biodata["pekerjaan"])  # Akan error → KeyError

print(biodata.get("pekerjaan"))               # None
print(biodata.get("pekerjaan", "Pelajar"))    # Pelajar
