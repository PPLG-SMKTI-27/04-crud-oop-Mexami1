class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

    def __repr__(self):
        return f"Buku(judul='{self.judul}', pengarang='{self.pengarang}', tahun_terbit={self.tahun_terbit})"


class Peminjaman:
    def __init__(self, buku, nama_peminjam, tanggal_pinjam, tanggal_kembali=None):
        self.buku = buku  # instance Buku
        self.nama_peminjam = nama_peminjam
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali

    def __repr__(self):
        return (f"Peminjaman(buku={self.buku.judul}, peminjam='{self.nama_peminjam}', "
                f"tanggal_pinjam='{self.tanggal_pinjam}', tanggal_kembali='{self.tanggal_kembali}')")



data_buku = [
    {"judul": "Python Dasar", "pengarang": "Budi", "tahun_terbit": 2019},
    {"judul": "Belajar AI", "pengarang": "Sari", "tahun_terbit": 2021},
    {"judul": "Algoritma", "pengarang": "Andi", "tahun_terbit": 2018}
]


list_buku = [Buku(**b) for b in data_buku]

print(list_buku)
