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
