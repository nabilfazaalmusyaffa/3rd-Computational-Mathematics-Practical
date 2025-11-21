A = {1, 2, 3}

# Menggunakan list comprehension untuk mencari pasangan yang memenuhi syarat
relasi = [(a, b) for a in A for b in A if a < b]

print("Pasangan dalam relasi 'lebih kecil dari':", relasi)