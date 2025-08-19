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

# Latihan 2: Class RekeningBank
# Buatlah sebuah class bernama RekeningBank untuk mensimulasikan rekening bank sederhana.
# -. Buat constructor __init__() yang menerima dua parameter: nomor_rekening dan
# nama_pemilik. Ia juga harus menginisialisasi atribut self.saldo dengan nilai awal 0.
# /. Buat method lihat_saldo() yang mencetak saldo saat ini.
# 0. Buat method setor(jumlah) yang menambahkan jumlah ke self.saldo dan mencetak pesan
# konfirmasi.
# 1. Buat method tarik(jumlah) yang mengurangi jumlah dari self.saldo. Tambahkan logika if di
# dalamnya: jika jumlah yang ditarik lebih besar dari saldo, cetak pesan "Saldo tidak mencukupi" dan
# jangan ubah saldo. Jika tidak, kurangi saldo dan cetak pesan konfirmasi.
# 3. Buat sebuah objek rekening_budi, lalu coba panggil semua method-nya: setor beberapa kali, tarik,
# dan lihat saldo.

print("-----Latihan 2-----")
class RekeningBank:
    def __init__(self, nomor_rekening, nama_pemilik, saldo=0):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo

    def lihat_saldo(self):
        print(f"Saldo {self.nama_pemilik}: Rp{self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Setor Rp{jumlah} berhasil. Saldonya sekarang jadi: Rp{self.saldo}")

    def tarik(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"Tarik Rp{jumlah} berhasil. Saldo sekarang jadi: Rp{self.saldo}")
        else:
            print("Saldo tidak mencukupi kalo mau penarikan.")
        

# Membuat objek rekening
rekening_budi = RekeningBank("123456789", "Budi")

# Uji coba transaksi
rekening_budi.lihat_saldo()
rekening_budi.setor(500000)
rekening_budi.tarik(200000)
rekening_budi.tarik(400000)  # coba tarik lebih besar dari saldo
rekening_budi.lihat_saldo()
