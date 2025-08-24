# Latihan untuk Menguji Pemahaman
# Waktunya membuat blueprint dan object pertamamu!

# Latihan 1: Class Kucing
# -. Buatlah sebuah class bernama Kucing.
# /. Buat constructor __init__() yang menerima dua parameter: nama dan warna. Constructor ini
# harus menyimpan nilai-nilai tersebut ke dalam atribut self.nama dan self.warna.
# 0. Buat sebuah method bernama bersuara() yang tidak memiliki parameter (selain self). Ketika
# dipanggil, method ini harus mencetak "Meow!".
# 1. Buat sebuah method bernama perkenalkan_diri() yang mencetak kalimat seperti "Halo, saya
# kucing bernama [nama] dan warna saya [warna].".
# 3. Buat dua object (instance) dari class Kucing dengan nama dan warna yang berbeda (misal, "Oren"
# berwarna "Oranye" dan "Milo" berwarna "Coklat").
# 4. Panggil method perkenalkan_diri() dan bersuara() dari kedua objek tersebut.

print("-----Latihan 1-----")
class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def bersuara(self):
        print("Meow!")

    def perkenalkan_diri(self):
        print(f"Meow!, saya kucing bernama {self.nama} dan warna saya {self.warna}.")        

# buat objek
kucing_oren = Kucing("Oyen", "oranye")
kucing_milo = Kucing("SiMeo", "coklat")
# coba method
kucing_oren.bersuara()
kucing_oren.perkenalkan_diri()

kucing_milo.bersuara()
kucing_milo.perkenalkan_diri()

