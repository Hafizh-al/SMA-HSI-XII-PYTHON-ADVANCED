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

