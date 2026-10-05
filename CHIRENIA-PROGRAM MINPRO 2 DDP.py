import os
import pwinput
from prettytable import PrettyTable

# DATA AKUN 

Akun = {
    "admin": {
        "password": "admincendana",
        "role": "admin"
    },
    "user": {
        "password": "usercendana",
        "role": "user"
    }
}

# DATA JADWAL TETAP DALAM LIST (SESUAI MINPRO 1)

Jadwal_Travel = [
    ["SENIN A", "08.00", "BALIKPAPAN/SAMARINDA", "KT 7080 BS", "PAK AHMAD"],
    ["SENIN B", "11.00", "BALIKPAPAN/SANGGATA", "KT 7090 BS", "PAK AMIR"],
    ["SELASA", "08.00", "BALIKPAPAN/SAMARINDA", "KT 7011 BS", "PAK UDIN"],
    ["RABU A", "08.00", "BALIKPAPAN/SAMARINDA", "KT 7015 BS", "PAK ANANG"],
    ["RABU B", "11.00", "BALIKPAPAN/SANGGATA", "KT 7010 BS", "PAK SATYA"],
    ["KAMIS", "08.00", "BALIKPAPAN/SAMARINDA", "KT 7119 BS", "PAK KUMIS"],
    ["JUMAT A", "08.00", "BALIKPAPAN/SAMARINDA", "KT 7080 BS", "PAK AHMAD"],
    ["JUMAT B", "11.00",  "BALIKPAPAN/SANGGATA", "KT 7090 BS", "PAK AMIR"],
    ["SABTU", "08.00", "BALIKPAPAN/SAMARINDA", "KT 7011 BS", "PAK UDIN"],
    ["MINGGU A", "08.00", "BALIKPAPAN/SAMARINDA", "KT 7015 BS", "PAK ANANG"],
    ["MINGGU B", "11.00", "BALIKPAPAN/SANGGATA", "KT 7010 BS", "PAK SATYA"]
]

# FUNCTION ULASAN

Ulasan = []

# FUNCTION MEMBERSIHKAN LAYAR

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

# FUNCTION INPUT TEKS

def input_data(pesan):
    while True:
        data = input(pesan).strip()

        if data != "":
            return data
        else:
            print("input tidak boleh kosong!")

# FUNCTION INPUT JAM

def input_jam(pesan):
    while True:
        jam = input(pesan).strip()

        if len(jam) == 5 and jam[2]  == "." :
            jam_sebelum = jam[:2]
            menit = jam[3:]

            try:
                jam_int = int(jam_sebelum)
                menit_int = int(menit)

                if 0 <= jam_int <= 23 and 0 <= menit_int <= 59:
                    return jam

            except ValueError:
                pass

        print("Format jam anda salah!")
        print("Gunakan format 24 jam, contoh : 08.00 atau 08.30")

# FUNCTION INPUT RUTE

def input_rute():
    while True:
        print("PILIH RUTE :")
        print("1. BALIKPAPAN/SAMARINDA")
        print("2. BALIKPAPAN/SANGGATA")

        pilihan = input("Pilih rute (1-2): ").strip()

        if pilihan == "1" :
            return "BALIKPAPAN/SAMARINDA"
        elif pilihan == "2" :
            return "BALIKPAPAN/SANGGATA"
        else:
            print("Pilihan tidak tersedia, silahkan pilih 1 atau 2")

# FUNCTION INPUT KONFIRMASI

def input_konfirmasi(pesan):

    while True:
        konfirmasi = input(pesan).strip().lower()

        if konfirmasi == "ya" :
            return True
        elif konfirmasi == "tidak" :
            return False
        else:
            print("Pilihan tidak tersedia, silahkan pilih ya/tidak.")

# FUNCTION INPUT LOGIN

def login():
    bersihkan_layar()

    print("=== LOGIN PENGGUNA ===")

    while True:
        username = input_data("Username:")
        password = pwinput.pwinput("Password:")

        if username in Akun:

            if password == Akun[username]["password"]:

                print("Anda berhasil login!")
                print("Selamat datang,", username)
                print("Role:", Akun[username]["role"])

                return {
                    "username": username,
                    "role": Akun[username]["role"]
                }

        print("Username atau password anda salah!")
        print("Silahkan coba kembali.")
            
# FUNCTION MENAMPILKAN JADWAL

def tampilkan_jadwal():
    bersihkan_layar()

    print("--JADWAL TRAVEL CENDANA TRAVEL BALIKPAPAN--")
    print("-TANGGAL 14 - 20 SEPTEMBER--")
    
    if len(Jadwal_Travel) == 0 :
        print("Belum ada jadwal keberangkatan.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "No",
        "Hari",
        "Jam",
        "Rute",
        "Plat Mobil",
        "Driver"
    ]

    nomor = 1

    for jadwal in Jadwal_Travel :
        tabel.add_row([
            nomor,
            jadwal[0],
            jadwal[1],
            jadwal[2],
            jadwal[3],
            jadwal[4]
        ])
        
        nomor += 1
    print(tabel)

# FUNCTION MEMERIKSA NAMA JADWAL

def jadwal_sudah_ada(hari, jam, nomor_dikecualikan=None):

    nomor = 0

    for jadwal in Jadwal_Travel:

        if nomor != nomor_dikecualikan:
        
            if jadwal[0].lower() == hari.lower() and jadwal[1] == jam:          
                return True

        nomor += 1

    return False

# FUNCTION MENAMBAHKAN JADWAL

def tambah_jadwal():
    bersihkan_layar()
    print("--- TAMBAH JADWAL ---")

    hari = input_data("Hari keberangkatan :")

    jam = input_jam("Jam keberangkatan (format 24 jam, contoh: 08.00 atau 08.30):")

    if jadwal_sudah_ada (hari, jam):
        print("Jadwal pada hari dan jam tersebut sudah ada!")
        return

    rute = input_rute()
    plat_mobil = input_data("Plat mobil:")

    driver = input_data("Nama driver:")

    jadwal_baru = [
        hari,
        jam,
        rute,
        plat_mobil,
        driver
    ]

    Jadwal_Travel.append(jadwal_baru)
    print("Jadwal baru berhasil di tambahkan:", Jadwal_Travel)

# FUNCTION MENGUBAH JADWAL

def ubah_jadwal():

    bersihkan_layar()

    tampilkan_jadwal()
    print("--- UBAH JADWAL ---")

    hari_dicari = input_data("Masukan hari/jadwal yang ingin anda ubah:").lower()

    ada_jadwal = False

    nomor = 0

    for jadwal in Jadwal_Travel:
        
        if jadwal[0].lower() == hari_dicari:

            ada_jadwal = True
            print("Jadwal yang dipilih:")
            print("Hari:", jadwal[0])
            print("Jam:", jadwal[1])
            print("Rute:", jadwal[2])
            print("Plat Mobil:", jadwal[3])
            print("Driver:", jadwal[4])

            while True:

                print("DATA YANG INGIN DI UBAH")
                print("1. Hari")
                print("2. Jam")
                print("3. Rute")
                print("4. Plat Mobil")
                print("5. Driver")
                print("6. Selesai")

                pilihan = input("Pilih menu (1-6) :").strip()

                if pilihan == "1":

                    hari_baru = input_data("Hari baru:").lower()

                    if jadwal_sudah_ada(hari_baru, jadwal[1], nomor):
                        print("jadwal pada hari dan jam tersebut sudah ada!")
                    else:
                        jadwal[0] = hari_baru
                        print("Hari berhasil diubah!")

                elif pilihan == "2":
                    jam_baru = input_jam("Jam baru (format 24 jam, contoh: 08.00 atau 08.30):")

                    if jadwal_sudah_ada(jadwal[0], jam_baru, nomor):
                        print("Jadwal pada hari dan jam tersebut sudah ada!")
                    else:
                        jadwal[1] = jam_baru
                        print("Jam berhasil diubah:",Jadwal_Travel)
                
                elif pilihan == "3":
                    jadwal[2] = input_rute()
                    print("Rute berhasil diubah:",Jadwal_Travel)
                elif pilihan == "4":
                    jadwal[3] = input_data("Plat mobil baru:").lower()
                    print("Plat mobil berhasil diubah:",Jadwal_Travel)
                elif pilihan == "5":
                    jadwal[4] = input_data("Nama driver baru:").lower()
                    print("Nama driver berhasil diubah:",Jadwal_Travel)
                elif pilihan == "6":
                    print("Anda kembali ke menu admin.")
                    break
                else:
                    print("Pilihan tidak tersedia, mohon periksa kembali.")
            
            break

        nomor += 1

    if ada_jadwal == False:
        print("Jadwal tidak di temukan, mohon periksa kembali.")

# FUNCTION MENGHAPUS JADWAL

def hapus_jadwal():
    bersihkan_layar()

    tampilkan_jadwal()
    print("--- HAPUS JADWAL ---")

    if len(Jadwal_Travel) == 0:
        return
    
    while True:

        pilihan = input("Masukan nomor jadwal yang ingin di hapus(sesuai urutan tabel):").strip()

        try:
            nomor = int(pilihan)

            if 1<= nomor <= len(Jadwal_Travel):
                break

        except ValueError:
            pass

        print("Nomor jadwal tidak sesuai, pilih nomor antara 1 - 11!")

    indeks = nomor - 1

    data = Jadwal_Travel[indeks]

    print("Jadwal yang akan dihapus:")
    print("Hari:", data[0])
    print("Jam:", data[1])
    print("Rute:", data[2])
    print("Plat Mobil:", data[3])
    print("Driver:", data[4])

    konfirmasi = input_konfirmasi("Anda yakin ingin menghapus jadwal ini?(ya/tidak):")

    if konfirmasi:
        Jadwal_Travel.pop(indeks)
        print("Jadwal berhasil dihapus!")
    else:
        print("Jadwal batal dihapus!")

# FUNCTION MEMBERIKAN ULASAN

def beri_ulasan(username):
    bersihkan_layar()
    print("--- BERIKAN ULASAN ---")

    teks_ulasan = input_data("Tuliskan ulasan anda:")
    data_ulasan = [
        username,
        teks_ulasan
        ]

    Ulasan.append(data_ulasan)

    print("ulasan berhasil di kirim, terimakasih atas ulasan anda!")

# FUNCTION MELIHAT ULASAN

def lihat_ulasan():
    bersihkan_layar()

    print("--- LIHAT ULASAN ---")

    if len(Ulasan) == 0:

        print("Belum ada ulasan dari user.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "No", 
        "Username", 
        "Ulasan"]
    
    nomor = 1

    for data in Ulasan:

        tabel.add_row([
            nomor,
            data[0],
            data[1]
        ])

        nomor += 1
    
    print(tabel)

# MENU ADMIN

def menu_admin():

    while True:

        bersihkan_layar()
        print("--- MENU ADMIN ---")
        print("1. Tambah Jadwal")
        print("2. Ubah Jadwal")
        print("3. Hapus Jadwal")
        print("4. Tampilkan Jadwal")
        print("5. Lihat Ulasan")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6):").strip()

        if pilihan == "1":
            tambah_jadwal()
            input("Tekan ENTER untuk kembali ke menu...")
        elif pilihan == "2":
            ubah_jadwal()
            input("Tekan ENTER untuk kembali ke menu...")
        elif pilihan == "3":
            hapus_jadwal()
            input("Tekan ENTER untuk kembali ke menu...")
        elif pilihan == "4":
            tampilkan_jadwal()
            input("Tekan ENTER untuk kembali ke menu...")
        elif pilihan == "5":
            lihat_ulasan()
            input("Tekan ENTER untuk kembali ke menu...")
        elif pilihan == "6":
            print("Anda keluar dari menu admin.")
            break
        else:
            print("Pilihan tidak tersedia, pilihan menu hanya 1-3")
            input("Tekan ENTER untuk kembali ke menu...")

# MENU USER

def menu_user(username):
    
    while True:
    
        bersihkan_layar()

        print("--- MENU USER ---")
        print("1. Tampilkan Jadwal")
        print("2. Beri Ulasan")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3):").strip()

        if pilihan == "1":
            tampilkan_jadwal()
            input("Tekan ENTER untuk kembali ke menu...")
        elif pilihan == "2":
            beri_ulasan(username)
            input("Tekan ENTER untuk kembali ke menu...")
        elif pilihan == "3":
            print("Anda keluar dari menu user.")
            break
        else:
            print("Pilihan tidak tersedia, pilihan menu hanya 1-3")
            input("Tekan ENTER untuk kembali ke menu...")

# PROGRAM UTAMA

def program_utama():

    while True:
        pengguna = login()

        if pengguna["role"] == "admin":
            menu_admin()
        elif pengguna["role"] == "user":
            menu_user(pengguna["username"])

# MENJALANKAN PROGRAM

program_utama()