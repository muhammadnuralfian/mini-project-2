database = {
    "produk": [
        {"id": 1, "nama": "Oli Motor", "harga": 50000},
        {"id": 2, "nama": "Ban Motor", "harga": 150000},
    ]
}

def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Logout")
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            lihat_produk()
        elif pilihan == "2":
            tambah_produk()
        elif pilihan == "3":
            update_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")

def menu_pembeli():
    while True:
        print("\n=== MENU PEMBELI ===")
        print("1. Lihat Produk")
        print("2. Beli Produk")
        print("3. Logout")

        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            lihat_produk()
        elif pilihan == "2":
            beli_produk()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak benar!")

def lihat_produk():
    print("\n=== DAFTAR PRODUK ===")
    for produk in database["produk"]:
        print(f"ID: {produk['id']}, Nama: {produk['nama']}, Harga: {produk['harga']}")

def tambah_produk():
    print("\n=== TAMBAH PRODUK ===")
    id_baru = len(database["produk"]) + 1
    nama_baru = input("Masukkan Nama barang: ")
    harga_baru = int(input("Masukkan Harga barang: "))

    produk_baru = {"id": id_baru, "nama": nama_baru, "harga": harga_baru}
    database["produk"].append(produk_baru)
    print(f"Produk {nama_baru} berhasil ditambahkan!")

def update_produk():
    print("\n=== UPDATE PRODUK ===")
    lihat_produk()
    id_produk = int(input("Masukkan ID Produk yang akan diupdate: "))
    
    for produk in database["produk"]:
        if produk["id"] == id_produk:
            produk["nama"] = input("tampilkan Nama Baru barang: ")
            produk["harga"] = int(input("tampilkan Harga Baru barang: "))
            print("Produk berhasil diupdate!")
            return
    print("ID Produk tidak ditemukan!")

def hapus_produk():
    print("\n=== HAPUS PRODUK ===")
    lihat_produk()
    id_produk = int(input("Masukkan ID Produk yang akan dihapus: "))
    
    for produk in database["produk"]:
        if produk["id"] == id_produk:
            database["produk"].remove(produk)
            print("Produk berhasil dihapus!")
            return
    print("ID Produk tidak ditemukan!")


def beli_produk():
    print("\n=== BELI PRODUK ===")
    lihat_produk()
    id_produk = int(input("Masukkan ID barang yang ingin dibeli: "))
    
    for produk in database["produk"]:
        if produk["id"] == id_produk:
            print(f"Anda membeli {produk['nama']} seharga {produk['harga']}")
            return
    print("ID Produk tidak ditemukan!")
# Login
Akun = {
    "Alfian": "12345",
    "Pian": "6789"
}

def login():
    print('+' + '-'* 76 + '+')
    print('| Selamat Datang! Di Sistem Manajemen Bengkel Alfian |')
    print('+' + '-'* 76 + '+')
    while True:
        Username = input("Username: ")
        Password = input("Password: ")
        if Username in Akun and Akun[Username] == Password:
            if Username == "Alfian":
                print('+' + '-'* 22 + '+')
                print('| Selamat Datang Admin |')
                print('+' + '-'* 22 + '+')
                menu_admin()
            else:
                print('+' + '-'* 49 + '+')
                print('| Halo, Selamat Datang Di Sistem Manajemen Benngkel Alfian |')
                print('+' + '-'* 49 + '+')
                menu_pembeli()
            break
        else:
            print("Username dan Password tidak sesuai, silahkan coba lagi")
# Contoh eksekusi
login()
