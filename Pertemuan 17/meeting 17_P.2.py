# Latihan 2: Immutability
# Diberikan tuple koordinat_awal = (10, 20). Tulis kode yang menghasilkan tuple baru bernama
# koordinat_baru yang nilainya (10, 25). Kamu tidak boleh mengubah koordinat_awal secara
# langsung.

print("_____Latihan 2_____")
tuple_koordinat_awal = (10, 20)
koordinat_baru = (tuple_koordinat_awal[0], 25)

print("Koordinat awal:", tuple_koordinat_awal)
print("Koordinat baru:", koordinat_baru)