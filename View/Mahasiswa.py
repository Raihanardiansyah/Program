class TampilMahasiswa:
    def tampilkan_daftar(self, data):
        print("Daftar Mahasiswa:")
        for m in data:
            print(f"NIM: {m.nim}, Nama: {m.nama}, Jurusan: {m.jurusan}")

    def tampilkan_detail(self, mahasiswa):
        if mahasiswa:
            print("Detail Mahasiswa:")
            print(f"NIM: {mahasiswa.nim}")
            print(f"Nama: {mahasiswa.nama}")
            print(f"Jurusan: {mahasiswa.jurusan}")
        else:
            print("Mahasiswa tidak ditemukan.")
