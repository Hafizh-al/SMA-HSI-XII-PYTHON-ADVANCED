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
