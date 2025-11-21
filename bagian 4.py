B = [1, 2, 4]
tabel_relasi = []

# Loop luar untuk baris (elemen i)
for i in B:
    row = []
    # Loop dalam untuk kolom (elemen j)
    for j in B:
        # Cek apakah j adalah kelipatan dari i (sisa bagi 0)
        if j % i == 0:
            row.append(1)
        else:
            row.append(0)
    tabel_relasi.append(row)

print("Tabel relasi kelipatan:")
for row in tabel_relasi:
    print(row)