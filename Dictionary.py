data_mahasiswa = {}

def tambah_data():
    """Menambahkan data mahasiswa ke dictionary."""
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    data_mahasiswa[nama] = nim
    print(f"Data {nama} berhasil ditambahkan.")

def hapus_data():
    """Menghapus data mahasiswa dari dictionary."""
    nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus.")
    else:
        print(f"Data {nama} tidak ditemukan.")

def tampilkan_data():
    """Menampilkan semua data mahasiswa dalam dictionary."""
    if data_mahasiswa:
        print("Data Mahasiswa:")
        for nama, nim in data_mahasiswa.items():
            print(f"Nama: {nama}, NIM: {nim}")
    else:
        print("Tidak ada data mahasiswa.")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Hapus Data Mahasiswa")
        print("3. Tampilkan Data Mahasiswa")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            hapus_data()
        elif pilihan == "3":
            tampilkan_data()
        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
