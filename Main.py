# Project 1: Bioskop Mini CLI
# Belajar: List, Dictionary, Function, File Handling

DATA_FILE = "data_film.txt"
daftar_film = []

def load_data():
    """Ambil data dari file.txt pas aplikasi dibuka"""
    global daftar_film
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                judul, genre, tahun = line.strip().split(",")
                film = {"judul": judul, "genre": genre, "tahun": tahun}
                daftar_film.append(film)
    except FileNotFoundError:
        pass 

def save_data():
    """Simpan data ke file.txt biar gak hilang"""
    with open(DATA_FILE, "w") as file:
        for film in daftar_film:
            file.write(f"{film['judul']},{film['genre']},{film['tahun']}\n")

def tambah_film():
    print("\n--- TAMBAH FILM BARU ---")
    judul = input("Judul Film: ")
    genre = input("Genre: ")
    tahun = input("Tahun Rilis: ")
    film_baru = {"judul": judul, "genre": genre, "tahun": tahun}
    daftar_film.append(film_baru)
    save_data()
    print(f"Film '{judul}' berhasil ditambahkan!")

def lihat_film():
    print("\n--- DAFTAR FILM ---")
    if not daftar_film:
        print("Belum ada film.")
        return
    for i, film in enumerate(daftar_film, 1):
        print(f"{i}. {film['judul']} | {film['genre']} | {film['tahun']}")

def cari_film():
    print("\n--- CARI FILM ---")
    keyword = input("Masukkan judul yang dicari: ").lower()
    hasil = [f for f in daftar_film if keyword in f['judul'].lower()]
    if hasil:
        for film in hasil:
            print(f"- {film['judul']} | {film['genre']} | {film['tahun']}")
    else:
        print("Film tidak ditemukan.")

def main():
    load_data() 
    while True:
        print("\n===== BIOSKOP MINI CLI =====")
        print("1. Lihat Semua Film")
        print("2. Tambah Film")
        print("3. Cari Film")
        print("4. Keluar")

        pilihan = input("Pilih menu 1-4: ")

        if pilihan == '1':
            lihat_film()
        elif pilihan == '2':
            tambah_film()
        elif pilihan == '3':
            cari_film()
        elif pilihan == '4':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
