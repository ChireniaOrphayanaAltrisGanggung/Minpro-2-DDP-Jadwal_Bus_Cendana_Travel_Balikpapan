# Minpro-2-DDP-Jadwal_Bus_Cendana_Travel_Balikpapan

NAMA : CHIRENIA ORPHAYANA ALTRIS GANGGUNG

NIM : 2609116038

KELAS : A SISTEM INFORMASI

**A. DESKRIPSI SINGKAT PROGRAM**

Program Jadwal Keberangkatan Bus Cendana Travel Balikpapan merupakan pengembangan dari Mini Project 1, Program ini digunakan untuk mengelola jadwal keberangkatan bus, mulai dari menambahkan, menampilkan, mengubah, hingga menghapus jadwal.

Program menggunakan list untuk menyimpan data jadwal dan dictionary untuk menyimpan informasi akun, password, serta role pengguna. Terdapat dua role, yaitu admin yang memiliki akses CRUD lengkap dan user yang dapat melihat jadwal serta memberikan ulasan.

Program juga menggunakan beberapa library Python, yaitu os untuk membersihkan layar, pwinput untuk menyembunyikan input password, dan PrettyTable untuk menampilkan data dalam bentuk tabel. Validasi input dan try-except diterapkan untuk membantu menangani masukan yang tidak sesuai.

**B. PENJELASAN SINGKAT ALUR FLOWCHART**

<img width="3512" height="1940" alt="MINPRO 2 FLOWCHART_CHIRENIA O A G drawio" src="https://github.com/user-attachments/assets/785a1213-a92b-4732-9598-1ebe25d38f6b" />

1. Flowchart dimulai dari menampilkan informasi program dan proses login menggunakan username serta password. Jika data login tidak sesuai, pengguna diminta menginput kembali. Jika berhasil, program memeriksa username dan role pengguna untuk menentukan menu yang dapat diakses.

2. Pada program ini terdapat 2 role pengguna yang dapat diakses :

   Admin: Menambahkan jadwal baru, mengubah data jadwal, menghapus jadwal, menampilkan jadwal, serta melihat ulasan dari user.

   User : menampilkan jadwal keberangkatan dan memberikan ulasan.

3. Setiap masing - masing proses dilengkapi validasi input agar pilihan dan data yang dimasukkan sesuai ketentuan :

   - Pada proses penghapusan, program meminta konfirmasi terlebih dahulu.

   - Setelah menyelesaikan suatu proses, pengguna dapat kembali ke menu sesuai rolenya.

   - Menu berakhir ketika pengguna memilih menu keluar.
  
**C. PENJELASAN KODE PROGRAM**

1. MENGIMPORT LIBARY

   <img width="405" height="109" alt="image" src="https://github.com/user-attachments/assets/3eb2af17-2061-48cd-9670-e0b506ab0062" />

   Program menggunakan 3 libary python yaitu **Libary OS**, digunakan untuk membersihkan tampilan terminal. **Libary pwinput**, digunakan untuk menyembunyi password saat melakukan
   login, sedangkan **PrettyTable** digunakan untuk menampilkan jadwal keberangkatan dan ulasan dalam bentuk tabel agar rapi.

2. DATA AKUN
  
   <img width="472" height="294" alt="image" src="https://github.com/user-attachments/assets/fa97f8a2-9b3e-4709-9306-07cb6b5ccecf" />

   Pada bagian ini, **Dictionary** akun di gunakan untuk menyimpan informasi akun pengguna yang terdiri dari username, password dan role. Program memiliki 2 role yaitu admin dan user,
   informasi role digunakan untuk menenentukan menu masing masing setelah berhasil login.

3. MENGGUNAKAN LIST

   <img width="724" height="359" alt="image" src="https://github.com/user-attachments/assets/53e14d74-4bb9-4f89-9fbf-9ef32115df55" />

   Data jadwal keberangkatan disimpan dalam list Jadwal_Travel berisi hari, jam, rute, plat mobil dan nama driver sesuai dengan Mini Project 1.

   <img width="248" height="103" alt="image" src="https://github.com/user-attachments/assets/6fef0273-4728-4807-968f-e37eac69c9e2" />

   Sementara itu, list Ulasan merupakan list kosong digunakan untuk menyimpan ulasan yang diberikan oleh user, ulasan terdiri dari username dan isi ulasan.

4. FUNCTION MEMBERSIHKAN LAYAR
  
   <img width="511" height="128" alt="image" src="https://github.com/user-attachments/assets/2402a4f8-83a5-4ada-8d10-b773110521e5" />

   Function bersihkan_layar() menggunakan **library OS** untuk membersihkan tampilan terminal, function digunakan pada beberapa bagian agar tampilan menu dan informasi lebih rapi saat
   perpindahan menu.

5. FUNCTION VALIDASI INPUT
   
   Program memiliki beberapa function untuk memvalidasi input pengguna, yaitu:

   - input_data() digunakan untuk menerima input teks dan memastikan input tidak kosong. Jika pengguna hanya menekan Enter atau memasukkan spasi, program akan meminta input kembali

     <img width="507" height="255" alt="image" src="https://github.com/user-attachments/assets/3114731f-35cb-4c1f-835a-e55137387d11" />

     
   - input_jam() digunakan untuk memvalidasi jam keberangkatan dengan format 24 jam, seperti 08.00 atau 13.30. Program memeriksa format, rentang jam, dan rentang menit. **try-except**
     digunakan untuk menangani kesalahan ketika input jam tidak dapat dikonversi menjadi bilangan bulat.

     <img width="662" height="524" alt="image" src="https://github.com/user-attachments/assets/f0c644d0-e20e-427a-a999-502af6b6ba38" />

     
   - input_rute() digunakan untuk memilih rute keberangkatan. Pengguna dapat memilih Balikpapan/Samarinda atau Balikpapan/Sanggata. Jika pilihan tidak sesuai, program meminta pengguna
     memilih kembali.

     <img width="651" height="387" alt="image" src="https://github.com/user-attachments/assets/d2f42ea1-757e-48aa-ac92-fbd85d74c53a" />


   - input_konfirmasi() digunakan untuk menerima konfirmasi ya atau tidak, misalnya ketika pengguna ingin menghapus jadwal. Jawaban menggunakan lower() agar semua input diubah ke huruf
     kecil.

     <img width="676" height="322" alt="image" src="https://github.com/user-attachments/assets/938aace4-945e-4e5f-bcdd-77949e972c6d" />

6. FUNCTION LOGIN

   <img width="664" height="590" alt="image" src="https://github.com/user-attachments/assets/8e6fbe20-9db0-4b82-a991-aec545176a80" />


   Function login() digunakan untuk memeriksa username dan password yang dimasukkan
   pengguna. Program mencocokkan data tersebut dengan informasi yang tersimpan dalam
   dictionary Akun. Jika data sesuai, program menampilkan pesan keberhasilan login dan
   mengembalikan informasi username serta role pengguna. Jika data tidak sesuai,
   program menampilkan pesan kesalahan dan meminta pengguna mencoba kembali.
   Pada bagian ini **libary pwinput** digunakan untuk menyembunyikan password yang dimasukan.

   OUTPUT PROGRAM :

   <img width="346" height="99" alt="image" src="https://github.com/user-attachments/assets/fbd302ec-1f62-4eb1-a81e-e13b2532beef" />

   OUTPUT PROGRAM JIKA PASSWORD DAN USERNAME SALAH :

   <img width="431" height="157" alt="image" src="https://github.com/user-attachments/assets/d968efc1-aa65-45aa-a39f-6c9330e2c0a1" />

7. MENAMPILKAN JADWAL

   Function jadwal_sudah_ada() digunakan untuk memeriksa apakah jadwal dengan hari dan
   jam yang sama sudah tersimpan. Pemeriksaan ini membantu mencegah penambahan atau
   perubahan jadwal yang memiliki kombinasi hari dan jam yang sama dengan jadwal lain.

   <img width="605" height="546" alt="image" src="https://github.com/user-attachments/assets/07e8b21b-08f6-4f44-8314-48f46420dd8a" />

   <img width="488" height="288" alt="image" src="https://github.com/user-attachments/assets/dc011f0c-e6f3-4913-b995-f653fce9008c" />

   Pada bagian ini **Libary PrettyTable** digunakan untuk menampilkan jadwal secara rapi dalam bentuk tabel.

   OUTPUT PROGRAM :

   <img width="751" height="412" alt="image" src="https://github.com/user-attachments/assets/53173c34-7b6c-4821-ada1-37ba3fda34f8" />

9. MENAMBAHKAN JADWAL

   Function tambah_jadwal() digunakan oleh admin untuk menambahkan jadwal
   keberangkatan baru. Admin memasukkan hari, jam, rute, plat mobil, dan nama driver.
   Program memvalidasi jam serta memeriksa apakah jadwal dengan hari dan jam tersebut
   sudah ada. Jika belum ada, data baru disusun dalam bentuk list dan ditambahkan ke
   Jadwal_Travel menggunakan append().

   <img width="693" height="379" alt="image" src="https://github.com/user-attachments/assets/27eb5f10-153a-4f46-a8e4-b7a407d838e4" />

   <img width="819" height="517" alt="image" src="https://github.com/user-attachments/assets/d09b0615-175b-49e7-8526-64183c5ec060" />

   <img width="691" height="176" alt="image" src="https://github.com/user-attachments/assets/47a91a2e-570b-43f0-b2e9-68e0ce183cda" />

   OUTPUT PROGRAM :

   <img width="1216" height="388" alt="image" src="https://github.com/user-attachments/assets/5e51aa1c-b231-4307-aef1-51a79cc37443" />

   OUTPUT PROGRAM JIKA JADWAL SUDAH ADA :

   <img width="689" height="185" alt="image" src="https://github.com/user-attachments/assets/184d5139-c2e9-4d9a-adc1-f15eeb78045c" />

10. MENGUBAH JADWAL

    Function ubah_jadwal() digunakan oleh admin untuk memperbarui informasi jadwal
    yang sudah tersimpan. Admin memilih jadwal berdasarkan nama hari atau jadwal yang
    tercantum, kemudian memilih bagian menu yang ingin diubah, yaitu hari, jam, rute,
    plat mobil, atau driver. Program memeriksa keberadaan jadwal dan mencegah
    perubahan hari atau jam yang menyebabkan duplikasi jadwal. Admin dapat memilih
    menu selesai untuk mengakhiri proses pengubahan.

    <img width="815" height="571" alt="image" src="https://github.com/user-attachments/assets/a176863e-855d-4222-9be2-c8d878175a67" />

    <img width="815" height="483" alt="image" src="https://github.com/user-attachments/assets/6c3c561e-face-4c62-bcc7-3c034ce6ce16" />

    <img width="917" height="534" alt="image" src="https://github.com/user-attachments/assets/4ac85c92-19ad-4035-89af-323d28d177e8" />

    <img width="707" height="268" alt="image" src="https://github.com/user-attachments/assets/e814922c-2deb-4ea1-a71c-1833b54604e9" />

    OUTPUT PROGRAM :

    <img width="853" height="623" alt="image" src="https://github.com/user-attachments/assets/77bd99ce-6c1e-46ba-9f10-b38a6abcfcdd" />

    <img width="1218" height="560" alt="image" src="https://github.com/user-attachments/assets/0d7a6570-0853-42bf-b8c5-70f0c4194c72" />

11. MENGHAPUS JADWAL

    Function hapus_jadwal() digunakan oleh admin untuk menghapus jadwal tertentu.
    Program menampilkan daftar jadwal, kemudian meminta admin memasukkan nomor jadwal
    yang ingin dihapus. Input nomor diperiksa menggunakan try-except agar masukan yang
    bukan bilangan bulat tidak langsung menghentikan program. Setelah nomor dinyatakan
    valid, program menampilkan detail jadwal dan meminta konfirmasi. Jika admin
    memilih ya, jadwal dihapus menggunakan pop(). Jika memilih tidak, penghapusan
    dibatalkan.

    





    





   











   
