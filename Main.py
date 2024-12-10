import sys
print("Current Python Path: ")
for path in sys.path:
    print(path)

from Data.Mahasiswa import Mahasiswa, DataMahasiswa
from View.input_form import InputForm
from View.Mahasiswa import TampilMahasiswa

data_mahasiswa = DataMahasiswa()
input_form = InputForm()
tampil_mahasiswa = TampilMahasiswa()

def menu_utama():
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Daftar Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = input_form.input_data()
            data_mahasiswa.tambah_data(Mahasiswa(nim, nama, jurusan))
        elif pilihan == "2":
            tampil_mahasiswa.tampilkan_daftar(data_mahasiswa.data)
        elif pilihan == "3":
            nim = input("Masukkan NIM Mahasiswa yang dicari: ")
            mahasiswa = data_mahasiswa.cari_data(nim)
            tampil_mahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == "4":
            nim = input("Masukkan NIM Mahasiswa yang akan diubah: ")
            nama = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
            jurusan = input("Masukkan Jurusan baru (kosongkan jika tidak diubah): ")
            data_mahasiswa.ubah_data(nim, nama or None, jurusan or None)
        elif pilihan == "5":
            nim = input("Masukkan NIM Mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus_data(nim)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu_utama()
