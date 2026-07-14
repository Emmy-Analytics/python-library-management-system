data = {

"cipuy29":{

"Nama":"Devina",
"No HP":"081234567890",
"Judul Buku":"Python Dasar",
"Tanggal Pinjam":"2026-06-01",
"Jatuh Tempo":"2026-06-15",
"Tanggal Kembali":"2026-06-17",
"Status":"Terlambat",
"Denda":20000,
"Stok":4,
"Perpanjangan":0
},

"manis12":{

"Nama":"Rully",
"No HP":"081234567891",
"Judul Buku":"SQL Fundamental",
"Tanggal Pinjam":"2026-06-05",
"Jatuh Tempo":"2026-06-19",
"Tanggal Kembali":"2026-06-18",
"Status":"Dikembalikan",
"Denda":0,
"Stok":3,
"Perpanjangan":3
},

"bae01":{

"Nama":"Sita",
"No HP":"081234567892",
"Judul Buku":"Machine Learning",
"Tanggal Pinjam":"2026-06-10",
"Jatuh Tempo":"2026-06-24",
"Tanggal Kembali":"",
"Status":"Dipinjam",
"Denda":0,
"Stok":2,
"Perpanjangan":5
},

"anar14":{

"Nama":"Ana",
"No HP":"081234567893",
"Judul Buku":"Deep Learning",
"Tanggal Pinjam":"2026-06-12",
"Jatuh Tempo":"2026-06-26",
"Tanggal Kembali":"2026-06-25",
"Status":"Dikembalikan",
"Denda":0,
"Stok":2,
"Perpanjangan":0
},

"yuyun28":{

"Nama":"Yuyun",
"No HP":"081234567894",
"Judul Buku":"Python Dasar",
"Tanggal Pinjam":"2026-06-10",
"Jatuh Tempo":"2026-06-24",
"Tanggal Kembali":"2026-06-27",
"Status":"Terlambat",
"Denda":10000,
"Stok":4,
"Perpanjangan":2
},

"cinta25":{

"Nama":"cinta",
"No HP":"081234567895",
"Judul Buku":"SQL Fundamental",
"Tanggal Pinjam":"2026-06-16",
"Jatuh Tempo":"2026-06-30",
"Tanggal Kembali":"",
"Status":"Dipinjam",
"Denda":0,
"Stok":3,
"Perpanjangan":0
},

"zakyz8":{

"Nama":"Zaky",
"No HP":"081234567896",
"Judul Buku":"Machine Learning",
"Tanggal Pinjam":"2026-05-01",
"Jatuh Tempo":"2026-05-15",
"Tanggal Kembali":"",
"Status":"Dibekukan",
"Denda":900000,
"Stok":2,
"Perpanjangan":7
},

"billabil8":{

"Nama":"Billa",
"No HP":"081234567897",
"Judul Buku":"Deep Learning",
"Tanggal Pinjam":"2026-04-10",
"Jatuh Tempo":"2026-04-24",
"Tanggal Kembali":"",
"Status":"Dibekukan",
"Denda":900000,
"Stok":2,
"Perpanjangan":0
},

"aci33":{

"Nama":"Cia",
"No HP":"081234567898",
"Judul Buku":"Python Dasar",
"Tanggal Pinjam":"2026-06-02",
"Jatuh Tempo":"2026-06-16",
"Tanggal Kembali":"2026-06-10",
"Status":"Dikembalikan",
"Denda":0,
"Stok":4,
"Perpanjangan":0
},

"danidani4":{

"Nama":"Zidan",
"No HP":"081234567899",
"Judul Buku":"SQL Fundamental",
"Tanggal Pinjam":"2026-06-13",
"Jatuh Tempo":"2026-06-27",
"Tanggal Kembali":"",
"Status":"Dipinjam",
"Denda":0,
"Stok":3,
"Perpanjangan":1
}

}

buku = {

"BK001":{
"Judul":"Python Dasar",
"Stok":10
},

"BK002":{
"Judul":"SQL Fundamental",
"Stok":8
},

"BK003":{
"Judul":"Machine Learning",
"Stok":6
},

"BK004":{
"Judul":"Deep Learning",
"Stok":5
},

"BK005":{
"Judul":"Data Science",
"Stok":4
},

"BK006":{
"Judul":"Excel Advanced",
"Stok":7
},

"BK007":{
"Judul":"Power BI",
"Stok":3
},

"BK008":{
"Judul":"Statistics",
"Stok":9
},

"BK009":{
"Judul":"Artificial Intelligence",
"Stok":5
},

"BK010":{
"Judul":"Clean Code",
"Stok":6
}

}

def menu():

    while True:

        print("="*50)
        print("MENU PEMINJAMAN BUKU".center(50))
        print("="*50)

        print("A. Informasi Umum")
        print("B. Tambahkan Data Baru")
        print("C. Ubah Data Saya")
        print("D. Hapus Data Saya")
        print("E. Keluar")

        pilihan = input("\nMasukkan Menu: ").upper()

        if pilihan == "A":
            submenu_a()

        elif pilihan == "B":
            submenu_b()

        elif pilihan == "C":
            submenu_c()

        elif pilihan == "D":
            submenu_d()

        elif pilihan == "E":
            print("Terima kasih telah berkunjung.")
            break

        else:
            print("Mohon maaf, menu tidak tersedia.")


def submenu_a():

    while True:

        print("="*50)
        print("INFORMASI UMUM".center(50))
        print("="*50)

        print("1. Tampilkan Seluruh Data Buku")
        print("2. Cari Data Peminjaman Saya")
        print("3. Lihat Aturan")
        print("4. Kembali")

        pilih = input("\nMasukkan Pilihan anda: ")

        if pilih == "1":
            tampilkan_buku()

        elif pilih == "2":
            cari_data()

        elif pilih == "3":
            aturan()

        elif pilih=="4":
            break

        else:
            print("Mohon maaf, pilihan tidak tersedia.")

def tampilkan_buku():

    print("="*50)
    print("DAFTAR BUKU".center(50))
    print("="*50)

    print(f'\n{"ID":^8}{"Judul":^32}{"Stok":^10}')
    print("-"*50)

    for id_buku, detail in buku.items():

        print(f'{id_buku:^8}{detail["Judul"]:^32}{detail["Stok"]:^10}')

def cari_data():

    while True:
        id_anggota = input("Masukkan ID Anggota: ")

        if id_anggota in data:

            print("="*50)
            print(f"{"ID":<20}: {id_anggota}")
            print(f"{"Nama":<20}: {data[id_anggota]["Nama"]}")
            print(f"{"No HP":<20}: {data[id_anggota]["No HP"]}")
            print(f"{"Judul Buku":<20}: {data[id_anggota]["Judul Buku"]}")
            print(f"{"Tanggal Pinjam":<20}: {data[id_anggota]["Tanggal Pinjam"]}")
            print(f"{"Jatuh Tempo":<20}: {data[id_anggota]["Jatuh Tempo"]}")
            print(f"{"Tanggal Kembali":<20}: {data[id_anggota]["Tanggal Kembali"]}")
            print(f"{"Status":<20}: {data[id_anggota]["Status"]}")
            print(f"{"Denda":<20}: {data[id_anggota]["Denda"]}")
            print(f"{"Perpanjangan":<20}: {data[id_anggota]["Perpanjangan"]}")

            lagi = input("\nCari data lagi? (Y/N): ").upper()
            if lagi == "N":
                break

        else:
            print("\nID tidak ditemukan.")
            input("\nTekan ENTER untuk kembali...")
            break

def aturan():

    print("\n")
    print("="*80)
    print("ATURAN PEMINJAMAN PERPUSTAKAAN".center(80))
    print("="*80)

    print("\n[1] ATURAN PEMINJAMAN")
    print("-"*80)

    print("• Lama peminjaman buku adalah 14 hari sejak tanggal peminjaman.")
    print("• Pengembalian tepat waktu tidak dikenakan denda.")
    print("• Buku boleh dikembalikan lebih cepat dari tanggal jatuh tempo.")
    print("• Setiap anggota hanya boleh meminjam 1 buku dalam satu waktu.")
    print("• Maksimal perpanjangan peminjaman adalah 7 hari.")
    
    print("\n[2] DENDA KETERLAMBATAN")
    print("-"*80)

    print("• Denda keterlambatan sebesar Rp10.000 per hari.")
    print("• Maksimal keterlambatan adalah 90 hari (3 bulan).")
    print("• Maksimal denda sebesar Rp900.000.")
    print("• Denda dibayarkan saat pengembalian buku.")

    print("\n[3] SANKSI")
    print("-"*80)

    print("• Terlambat lebih dari 90 hari dianggap menghilangkan buku.")
    print("• Status anggota akan berubah menjadi 'Dibekukan'.")
    print("• Anggota tidak dapat meminjam buku kembali sebelum denda lunas.")
    print("• Setelah denda dibayar, status anggota dapat diaktifkan kembali.")

    print("\n")
    input("Tekan ENTER untuk kembali...")


def submenu_b():

    while True:

        print("="*50)
        print("TAMBAHKAN DATA BARU".center(50))
        print("="*50)

        print("1. Daftar Sebagai Anggota Baru")
        print("2. Permintaan Pengadaan Buku")
        print("3. Kembali ke Menu Utama")

        pilih = input("\nMasukkan Pilihan anda: ")

        if pilih == "1":
            daftar_anggota()

        elif pilih == "2":
            pengadaan_buku()

        elif pilih == "3":
            break

        else:
            print("Mohon maaf, pilihan tidak tersedia.")

def daftar_anggota():

    print("="*30)
    print("DAFTAR ANGGOTA BARU".center(30))
    print("="*30)

    id_anggota = input(f"{"Masukkan ID Anggota":<20}: ")

    if id_anggota in data:
        print("\nID sudah terdaftar.")
        input("Tekan ENTER untuk kembali...")
        return

    nama = input(f"{"Masukkan Nama":<20}: ")
    no_hp = input(f"{"Masukkan Nomor HP":<20}: ")

    while True:
        
        print("\n")
        print("="*30)
        print("APAKAH DATA INGIN DISIMPAN?".center(30))
        print("="*30)
        print("1. Ya")
        print("2. Tidak")
    
        pilih = input("\nMasukkan Pilihan: ")

        if pilih == "1":

            data[id_anggota] = {
                
                "Nama": nama,
                "No HP": no_hp,
                "Judul Buku": "",
                "Tanggal Pinjam": "",
                "Jatuh Tempo": "",
                "Tanggal Kembali": "",
                "Status": "Belum Meminjam",
                "Denda": 0,
                "Stok": 0,
                "Perpanjangan": 0

            }

            print("\n")
            print("="*30)
            print("DATA BERHASIL DITAMBAHKAN".center(30))
            print("="*30)

            print(f"{"ID":<20}: {id_anggota}")
            print(f"{"Nama":<20}: {nama}")
            print(f"{"No HP":<20}: {no_hp}")
            print(f"{"Status":<20}: Belum Meminjam")

            print("="*30)

            input("\nTekan ENTER untuk kembali...")
            break


        elif pilih == "2":

            print("\nData batal disimpan.")
            input("\nTekan ENTER untuk kembali...")
            break

        else:

            print("\nPilihan tidak tersedia.")
            print("\nApakah ingin memilih kembali?")
            print("1. Ya")
            print("2. Tidak")

            ulang = input("\nMasukkan Pilihan: ")

            if ulang == "2":

                print("\nData batal disimpan.")
                input("\nTekan ENTER untuk kembali...")
                break

            elif ulang == "1":
                continue

            else:

                print("\nInput tidak valid.")
                print("Data batal disimpan.")
                input("\nTekan ENTER untuk kembali...")
                break

def pengadaan_buku():

    print("="*30)
    print("PERMINTAAN PENGADAAN BUKU".center(30))
    print("="*30)

    nama = input(f"{"Nama Pengusul":<20}: ")
    judul = input(f"{"Judul Buku":<20}: ")
    alasan = input(f"{"Alasan":<20}: ")

    print("\nPermintaan berhasil dicatat.")
    print("="*30)
    print("RINGKASAN PERMINTAAN".center(30))
    print("="*30)
    print(f"{"Nama Pengusul":<20}: {nama}")
    print(f"{"Judul Buku":<20}: {judul}")
    print(f"{"Alasan":<20}: {alasan}")
    input("\nTekan ENTER untuk kembali...")


def submenu_c():

    while True:

        print("="*50)
        print("UBAH DATA".center(50))
        print("="*50)

        print("1. Ubah Data Saya")
        print("2. Perpanjang Masa Peminjaman Buku")
        print("3. Kembali ke Menu Utama")

        pilih = input("\nMasukkan Pilihan Anda : ")

        if pilih == "1":
            ubah_data()
        elif pilih == "2":
            perpanjang_peminjaman()
        elif pilih == "3":
            break

        else:
            print("\nPilihan tidak tersedia.")

def ubah_data():

    id_anggota = input("\nMasukkan ID Anggota: ")

    if id_anggota not in data:
        print("\nID tidak ditemukan.")
        input("\nTekan ENTER untuk kembali...")
        return

    # Menampilkan data lama
    print("="*30)
    print("DATA ANGGOTA".center(30))
    print("="*30)
    print(f"{"ID":<15}: {id_anggota}")
    print(f"{"Nama":<15}: {data[id_anggota]["Nama"]}")
    print(f"{"No HP":<15}: {data[id_anggota]["No HP"]}")
    print("="*30)


    while True:

        konfirmasi = input("\nApakah ingin mengubah data? (Y/N): ").upper()

        if konfirmasi == "Y":
           break

        elif konfirmasi == "N":
            print("\nPerubahan dibatalkan.")
            input("\nTekan ENTER untuk kembali...")
            return

        else:
            print("\nPilihan tidak tersedia.")
            print("\nApakah ingin memilih kembali?")
            print("1. Ya")
            print("2. Tidak")

            ulang = input("\nMasukkan Pilihan: ")

            if ulang == "1":
                continue

            elif ulang == "2":
                print("\nPerubahan dibatalkan.")
                input("\nTekan ENTER untuk kembali...")
                return

            else:
                print("\nInput tidak valid.")
                input("\nTekan ENTER untuk kembali...")
                return

    while True:

        print("="*30)
        print("PILIHAN DATA YANG INGIN DIUBAH".center(30))
        print("="*30)
        print("1. ID Anggota")
        print("2. Nama")
        print("3. Nomor HP")
        print("4. Kembali")

        pilih = input("\nMasukkan Pilihan: ")

        if pilih == "1":

            id_baru = input("Masukkan ID Baru: ")

            if id_baru in data:
                print("\nID sudah digunakan.")

            else:
                while True:
                    print("\n" + "="*30)
                    print("KONFIRMASI PERUBAHAN DATA".center(30))
                    print("="*30)
                    print(f'{"Field":<15}: ID Anggota')
                    print(f'{"ID Lama":<15}: {data[id_anggota]["Nama"]}')
                    print(f'{"ID Baru":<15}: {id_baru}')
                    print("="*30)

                    konfirmasi = input("\nApakah ingin mengubah data? (Y/N): ").upper()

                    if konfirmasi == "Y":

                        data[id_baru] = data.pop(id_anggota)
                        id_anggota = id_baru
                        print("\nID berhasil diperbarui.")
                        input("\nTekan ENTER untuk kembali...")
                        break

                    elif konfirmasi == "N":
                        print("\nPerubahan dibatalkan.")
                        input("\nTekan ENTER untuk kembali...")
                        break

                    else:
                        print("\nPilihan tidak tersedia.")
                        print("\nApakah ingin memilih kembali?")
                        print("1. Ya")
                        print("2. Tidak")

                        ulang = input("\nMasukkan Pilihan : ")

                        if ulang == "1":
                            continue

                        elif ulang == "2":
                            print("\nPerubahan dibatalkan.")
                            input("\nTekan ENTER untuk kembali...")
                            break

                        else:
                            print("\nInput tidak valid.")
                            print("Perubahan dibatalkan.")
                            input("\nTekan ENTER untuk kembali...")
                            break
    
        elif pilih == "2":

            nama_baru = input("Masukkan Nama Baru: ")

            while True:
                print("\n" + "="*30)
                print("KONFIRMASI PERUBAHAN DATA".center(30))
                print("="*30)
                print(f'{"Field":<15}: Nama')
                print(f'{"Nama Lama":<15}: {data[id_anggota]["Nama"]}')
                print(f'{"Nama Baru":<15}: {nama_baru}')
                print("="*30)

                konfirmasi = input("\nApakah ingin mengubah data? (Y/N): ").upper()

                if konfirmasi == "Y":

                    data[id_anggota]["Nama"] = nama_baru
                    print("\nNama berhasil diperbarui.")
                    input("\nTekan ENTER untuk kembali...")
                    break

                elif konfirmasi == "N":
                    print("\nPerubahan dibatalkan.")
                    input("\nTekan ENTER untuk kembali...")
                    break

                else:
                    print("\nPilihan tidak tersedia.")
                    print("\nApakah ingin memilih kembali?")
                    print("1. Ya")
                    print("2. Tidak")

                    ulang = input("\nMasukkan Pilihan : ")

                    if ulang == "1":
                        continue

                    elif ulang == "2":
                        print("\nPerubahan dibatalkan.")
                        input("\nTekan ENTER untuk kembali...")
                        break

                    else:
                        print("\nInput tidak valid.")
                        print("Perubahan dibatalkan.")
                        input("\nTekan ENTER untuk kembali...")
                        break
    
        elif pilih == "3":

            nomor_baru = input("Masukkan Nomor HP Baru: ")

            while True:
                print("\n" + "="*30)
                print("KONFIRMASI PERUBAHAN DATA".center(30))
                print("="*30)
                print(f'{"Field":<15}: Nomor HP')
                print(f'{"Nomor HP Lama":15}: {data[id_anggota]["No HP"]}')
                print(f'{"Nomor HP Baru":<15}: {nomor_baru}')
                print("="*30)

                konfirmasi = input("\nApakah ingin mengubah data? (Y/N): ").upper()

                if konfirmasi == "Y":

                    data[id_anggota]["No HP"] = nomor_baru
                    print("\nNomor HP berhasil diperbarui.")
                    input("\nTekan ENTER untuk kembali...")
                    break

                elif konfirmasi == "N":
                    print("\nPerubahan dibatalkan.")
                    input("\nTekan ENTER untuk kembali...")
                    break

                else:
                    print("\nPilihan tidak tersedia.")
                    print("\nApakah ingin memilih kembali?")
                    print("1. Ya")
                    print("2. Tidak")

                    ulang = input("\nMasukkan Pilihan : ")

                    if ulang == "1":
                        continue

                    elif ulang == "2":
                        print("\nPerubahan dibatalkan.")
                        input("\nTekan ENTER untuk kembali...")
                        break

                    else:
                        print("\nInput tidak valid.")
                        print("Perubahan dibatalkan.")
                        input("\nTekan ENTER untuk kembali...")
                        break
    
        elif pilih == "4":
            break

        else:
            print("\nPilihan tidak tersedia.")
            input("\nTekan ENTER untuk kembali...")
            continue
        
def perpanjang_peminjaman():

    id_anggota = input("\nMasukkan ID Anggota: ")

    if id_anggota not in data:
        print("\nID tidak ditemukan.")
        input("\nTekan ENTER untuk kembali...")
        return
   
    status = data[id_anggota]["Status"]

    if status == "Dikembalikan":
        print("\nBuku sudah dikembalikan.")
        input("\nTekan ENTER untuk kembali...")
        return

    elif status == "Belum Meminjam":
        print("\nBelum ada buku yang sedang dipinjam.")
        input("\nTekan ENTER untuk kembali...")
        return

    elif status == "Terlambat":
        print("\nTidak dapat memperpanjang.")
        print("Masih memiliki denda.")
        print("Mohon segera membayar denda terlebih dahulu.")
        input("\nTekan ENTER untuk kembali...")
        return

    elif status == "Dibekukan":
        print("\n" + "="*30)
        print("STATUS KEANGGOTAAN DIBEKUKAN".center(30))
        print("="*30)
        print("Anggota tidak dapat meminjam atau memperpanjang masa peminjaman.")
        print("Mohon segera membayar seluruh denda dan mengembalikan buku.")
        print("Terima kasih.")
        input("\nTekan ENTER untuk kembali...")
        return
    
    print("="*30)
    print("DATA PEMINJAMAN".center(30))
    print("="*30)
    print(f"{"ID":<20}: {id_anggota}")
    print(f"{"Nama":<20}: {data[id_anggota]["Nama"]}")
    print(f"{"Judul Buku":<20}: {data[id_anggota]["Judul Buku"]}")
    print(f"{"Tanggal Pinjam":<20}: {data[id_anggota]["Tanggal Pinjam"]}")
    print(f"{"Jatuh Tempo":<20}: {data[id_anggota]["Jatuh Tempo"]}")

    while True: #konfirmasi perpanjangan

        konfirmasi = input("\nApakah ingin memperpanjang masa peminjaman? (Y/N): ").upper()

        if konfirmasi == "Y":
            break

        elif konfirmasi == "N":
            print("\nPerpanjangan dibatalkan.")
            input("\nTekan ENTER untuk kembali...")
            return

        else:
            print("\nPilihan tidak tersedia.")
            print("\nApakah ingin memilih kembali?")
            print("1. Ya")
            print("2. Tidak")

            ulang = input("\nMasukkan Pilihan: ")

            if ulang == "2":

                print("\nData batal disimpan.")
                input("\nTekan ENTER untuk kembali...")
                return

            elif ulang == "1":
                continue

            else:

                print("\nInput tidak valid.")
                print("Data batal disimpan.")
                input("\nTekan ENTER untuk kembali...")
                return
            
    if data[id_anggota]["Perpanjangan"] >= 7:
        print("\nPerpanjangan sudah mencapai batas maksimal.")
        input("\nTekan ENTER untuk kembali...")
        return

    while True: #jumlah permohonan perpanjangan hari

        try:
            hari = int(input("\nMasukkan jumlah hari perpanjangan (maksimal 7hari): "))

        except:
            print("\nMasukkan angka.")
            continue

        if hari < 0:
            print("Jumlah hari tidak valid.")
            continue

        total = data[id_anggota]["Perpanjangan"] + hari

        if total > 7:
            print("\nPerpanjangan melebihi batas maksimal.")
            sisa = 7 - data[id_anggota]["Perpanjangan"]
            print(f"Anda hanya dapat menambah {sisa} hari lagi.")
            continue
         
        else:
            break

    while True: #konfirmasi simpan perpanjangan

        simpan = input("\nSimpan perpanjangan? (Y/N): ").upper()

        if simpan == "Y":
            data[id_anggota]["Perpanjangan"] = total
            print("\nPerpanjangan berhasil disimpan.")
            print(f"Masa peminjaman bertambah {hari} hari.")
            input("\nTekan ENTER untuk kembali...")
            return

        elif simpan == "N":
            print("\nPerpanjangan dibatalkan.")
            input("\nTekan ENTER untuk kembali...")
            return
        
        else:
            print("\nPilihan tidak tersedia.")
            print("Apakah ingin memilih kembali?")
            print("1. Ya")
            print("2. Tidak")

            ulang = input("\nMasukkan Pilihan : ")

            if ulang == "1":
                continue

            elif ulang == "2":
                print("\nPerpanjangan dibatalkan.")
                input("\nTekan ENTER untuk kembali...")
                return


def submenu_d():

    while True:

        print("="*50)
        print("HAPUS DATA".center(50))
        print("="*50)

        print("1. Hapus Keanggotaan Saya")
        print("2. Kembali")

        pilih = input("\nMasukkan Pilihan Anda : ")

        if pilih == "1":
            hapus_data()

        elif pilih == "2":
            break

        else:
            print("\nPilihan tidak tersedia.")

def hapus_data():

    id_anggota = input("\nMasukkan ID Anggota: ")

    if id_anggota not in data:
        print("\nID tidak ditemukan.")
        input("\nTekan ENTER untuk kembali...")
        return

    status = data[id_anggota]["Status"]
    denda = data[id_anggota]["Denda"]

    if status == "Dipinjam":
        print("\nAnggota masih meminjam buku.")
        print("Data tidak dapat dihapus.")
        input("\nTekan ENTER untuk kembali...")
        return

    elif status == "Terlambat":
        print("\nAnggota masih memiliki denda.")
        print("Mohon segera membayar denda terlebih dahulu.")
        print("Data tidak dapat dihapus.")
        input("\nTekan ENTER untuk kembali...")
        return

    elif status == "Dibekukan":
        print("\nStatus keanggotaan dibekukan.")
        print("Data tidak dapat dihapus.")
        input("\nTekan ENTER untuk kembali...")
        return

    elif denda > 0:
        print("\nMasih memiliki denda.")
        print("Data tidak dapat dihapus.")
        input("\nTekan ENTER untuk kembali...")
        return

    print("="*30)
    print("KONFIRMASI PENGHAPUSAN DATA".center(30))
    print("="*30)
    print(f"{'ID':<15}: {id_anggota}")
    print(f"{'Nama':<15}: {data[id_anggota]['Nama']}")
    print(f"{'No HP':<15}: {data[id_anggota]['No HP']}")
    print(f"{'Status':<15}: {data[id_anggota]['Status']}")
    print("="*30)

    while True:

        konfirmasi = input("\nApakah ingin menghapus data? (Y/N): ").upper()

        if konfirmasi == "Y":
            del data[id_anggota]
            print("\nData berhasil dihapus.")
            input("\nTekan ENTER untuk kembali...")
            return

        elif konfirmasi == "N":
            print("\nPenghapusan dibatalkan.")
            input("\nTekan ENTER untuk kembali...")
            return

        else:
            print("\nPilihan tidak tersedia.")
            print("Apakah ingin memilih kembali?")
            print("1. Ya")
            print("2. Tidak")

            ulang = input("\nMasukkan Pilihan: ")

            if ulang == "1":
                continue

            elif ulang == "2":
                print("\nPenghapusan dibatalkan.")
                input("\nTekan ENTER untuk kembali...")
                return

            else:
                print("\nInput tidak valid.")
                input("\nTekan ENTER untuk kembali...")
                return


menu()
