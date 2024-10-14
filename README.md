# mini-project-2

CODINGAN

![Cuplikan layar 2024-10-15 015009](https://github.com/user-attachments/assets/eac4a1a6-093a-4f1e-af47-fc433ef5cd23)
![Cuplikan layar 2024-10-15 015035](https://github.com/user-attachments/assets/84d374c5-d73c-460f-9d40-09ca86fa5e9a)
![Cuplikan layar 2024-10-15 015058](https://github.com/user-attachments/assets/f8fe67d0-b4bd-48d0-9c22-84eb9de2b0ec)
![Cuplikan layar 2024-10-15 015115](https://github.com/user-attachments/assets/9c1937c4-8383-49b0-a7e1-fe9c0fd333f9)
![Cuplikan layar 2024-10-15 015146](https://github.com/user-attachments/assets/193b49df-f46f-470b-a1ff-d58ec4870d4b)

Library yang digunakan:

getpass: Digunakan untuk input password tanpa menampilkannya di layar.
Database Produk:

Data produk disimpan dalam database, yang merupakan daftar produk berupa kamus dengan informasi id, nama, dan harga.
User Login:

Ada dua jenis pengguna: admin dan pembeli. Keduanya memiliki username dan password yang disimpan dalam users.
Fungsi login() meminta username dan password dari pengguna, lalu memverifikasi apakah data tersebut sesuai dengan data yang ada di users.
Menu untuk Admin dan Pembeli:

Admin memiliki akses ke berbagai fungsi manajemen produk: melihat, menambah, mengupdate, dan menghapus produk.
Pembeli hanya bisa melihat produk dan melakukan pembelian.
Fungsi-fungsi seperti menu_admin() dan menu_pembeli() digunakan untuk menampilkan opsi berdasarkan jenis pengguna yang login.
Fungsi Produk:

lihat_produk(): Menampilkan semua produk yang ada di database.
tambah_produk(): Admin bisa menambahkan produk baru.
update_produk(): Admin bisa memperbarui nama dan harga produk yang ada.
hapus_produk(): Admin bisa menghapus produk berdasarkan ID.
beli_produk(): Pembeli bisa memilih produk yang ingin dibeli berdasarkan ID.
Fungsi Utama:

Fungsi main() adalah titik awal program yang mengatur proses login dan mengarahkan pengguna ke menu admin atau pembeli berdasarkan perannya.
Jadi, kode ini memungkinkan admin untuk mengelola produk, sementara pembeli bisa melihat dan membeli produk dalam konteks sistem manajemen bengkel.


flowchart

![Cuplikan layar 2024-10-15 013214](https://github.com/user-attachments/assets/79d5f69c-0cc9-4461-b81e-8985d5490cd9)

