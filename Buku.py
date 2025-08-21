class Buku:
    def __init__(self, id_buku, judul, penulis, tahun_terbit):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def __repr__(self):
        return f"Buku({self.id_buku}, {self.judul}, {self.penulis}, {self.tahun_terbit})"


class Peminjaman:
    def __init__(self, id_peminjaman, buku, nama_peminjam, tanggal_pinjam, tanggal_kembali=None):
        self.id_peminjaman = id_peminjaman
        self.buku = buku            # Objek Buku
        self.nama_peminjam = nama_peminjam
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali

    def __repr__(self):
        return (f"Peminjaman({self.id_peminjaman}, {self.buku.judul}, "
                f"{self.nama_peminjam}, {self.tanggal_pinjam}, {self.tanggal_kembali})")


list_buku_dict = [
    {'id_buku': 1, 'judul': 'Python untuk Pemula', 'penulis': 'Andi', 'tahun_terbit': 2020},
    {'id_buku': 2, 'judul': 'Belajar Data Science', 'penulis': 'Budi', 'tahun_terbit': 2021},
]

list_buku_obj = [Buku(**data) for data in list_buku_dict]

print(list_buku_obj)
