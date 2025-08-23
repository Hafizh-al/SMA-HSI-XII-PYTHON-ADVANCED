# Latihan 4: Memahami Aliasing
# Prediksikan output dari kode di bawah ini sebelum menjalankannya. Jelaskan mengapa outputnya seperti
# itu.
# a = [1, 2, 3, 4, 5]
# b = a
# c = a.copy()
# b[1] = 20
# c[1] = 30
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")

a = [1, 2, 3, 4, 5]
b = a
c = a.copy()
b[1] = 20
c[1] = 30
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")