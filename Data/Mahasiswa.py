class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_data(self, nim, nama=None, jurusan=None):
        for m in self.data:
            if m.nim == nim:
                if nama:
                    m.nama = nama
                if jurusan:
                    m.jurusan = jurusan

    def cari_data(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None