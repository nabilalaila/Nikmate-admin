import os
import admin
import petugasnikah
import transaksi
import paketnikah
from datetime import datetime, timedelta

def login():
    os.system("cls")
    print("Hai! Selamat Datang di NikMate App 👋".center(115))
    global username
    username = input('Username: ')
    password = input('Password: ')
    adaUser = False
    for data in admin.readadmin():
        if username == data[0] and password == data[1]:
            adaUser = True
            break
    if adaUser == True:
        menuadmin()
    else:
        input('Yah, username/password yang kamu masukkan salah. Coba lagi yuk 🙌\nTekan enter untuk lanjut => ')
        os.system("cls")
        login()

def menuadmin():
    os.system("cls")
    print("Selamat datang di menu admin. Pilih menu yang kamu inginkan\n".center(115))
    menu_admin = input("|1| Input Reservasi\n|2| Tambah data petugas pernikahan\n|3| Hapus data petugas Pernikahan\n|4| Edit data petugas pernikahan\n|5| Konfirmasi Pembayaran Reservasi\n|6| Lihat Jadwal Pernikahan Hari Ini dan Besok \n|7| Cari Riwayat Reservasi\n|8| Keluar Aplikasi\nPilih => ")
    if menu_admin == "1":
        reservasi()
    elif menu_admin == "2":
        menu_tambahpetugas()
    elif menu_admin == "3":
        hapus_data_petugas()
    elif menu_admin == "4":
        menu_edit_petugas()
    elif menu_admin == "5":
        konfirmasi_pembayaran()
    elif menu_admin == "6":
        lihatjadwal()
    elif menu_admin == "7":
        caririwayatreservasi()
    elif menu_admin == "8":
        close()
    else:
        input("Maaf, inputanmu salah. Klik enter untuk lanjut => ")
        menuadmin()

def menu_tambahpetugas():
    input_data_petugas()
    tambah_petugasbaru()

def input_data_petugas():
    os.system("cls")
    global petugas_baru, nama_petugas, telp_petugas, honorarium_petugas, jenis_petugas
    print("Tambah data petugas pernikahan".center(115))
    nama_petugas = input("Nama Lengkap Petugas  : ")
    telp_petugas = input("Nomor Telepon Petugas : ")
    while (len(telp_petugas) > 12) or (telp_petugas.isdigit() == False):
        os.system("cls")
        print("Maaf, nomor telepon tidak boleh lebih dari 12 karakter dan harus berupa angka\n".center(115))
        telp_petugas = input(f"Nama Lengkap Petugas  : {nama_petugas}\nNomor Telepon Petugas : ")
    honorarium_petugas = input("Honorarium Petugas    : ")
    while honorarium_petugas.isdigit() is False:
        os.system("cls")
        print("Maaf, honorarium harus berupa angka\n".center(115))
        print(f"Nama Lengkap Petugas  : {nama_petugas}\nNomor Telepon Petugas : {telp_petugas}")
        honorarium_petugas = input("Honorarium Petugas    : ")
    jenis_petugas = input("Pilih jenis petugas :\n  a) MC\n  b) Tim Hadrah\n  c) Qori'\n  d) Mubaligh\n  Pilih: ")
    if jenis_petugas == "a":
        jenis_petugas = "1"
    elif jenis_petugas == "b":
        jenis_petugas = "2"
    elif jenis_petugas == "c":
        jenis_petugas = "3"
    elif jenis_petugas == "d":
        jenis_petugas = "4"
    else:
        input("Maaf, inputanmu salah. Klik enter untuk lanjut =>")
        input_data_petugas()
    petugas_baru = {'nama_petugas': nama_petugas, 'no_telp' : telp_petugas, 'Honorarium': honorarium_petugas, 'jenis_petugas' : jenis_petugas}
    
def tambah_petugasbaru():
    petugasnikah.writepetugas(petugas_baru)
    os.system("cls")
    input("Penambahan data petugas pernikahan berhasil\nKlik enter untuk lanjut => ".center(115))
    close()

def hapus_data_petugas():
    os.system("cls")
    print("Pilih data petugas yang ingin dihapus\n".center(115))
    for petugas in petugasnikah.readpetugas():
        print(f"{petugas[0]}. Nama Lengkap Petugas  : {petugas[1]}\n   Nomor Telepon Petugas : {petugas[2]}\n   Honorarium Petugas    : {petugas[3]}\n   Jenis Petugas         : {petugas[4]}\n")
    data_dihapus = input("Pilih Petugas (Ketik nomornya) : ")
    while data_dihapus.isdigit() == False:
        os.system("cls")
        print("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
        hapus_data_petugas()
    hapus = {'id' : int(data_dihapus)}
    petugasnikah.deletepetugas(hapus)
    input("Penambahan data petugas pernikahan berhasil\nKlik enter untuk lanjut => ".center(115))
    close()

def menu_edit_petugas():
    edit_data_petugas()
    update_petugas()

def edit_data_petugas():
    os.system("cls")
    print("Pilih data petugas yang ingin diubah\n".center(115))
    for petugas in petugasnikah.readpetugas():
        print(f"{petugas[0]}. Nama Lengkap Petugas  : {petugas[1]}\n   Nomor Telepon Petugas : {petugas[2]}\n   Honorarium Petugas    : {petugas[3]}\n   Jenis Petugas         : {petugas[4]}\n")
    global data_diedit
    data_diedit = input("Pilih Petugas (Ketik nomornya) : ")
    while data_diedit.isdigit() == False:
        os.system("cls")
        input("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
        edit_data_petugas()
    os.system("cls")
    print("Masukkan data petugas yang baru".center(115))
    input_data_petugas()
    
def update_petugas():
    petugas_baru['id'] = int(data_diedit)
    petugasnikah.updatepetugas(petugas_baru)
    os.system("cls")
    input("Edit data petugas pernikahan berhasil\nKlik enter untuk lanjut => ".center(115))
    close()

def konfirmasi_pembayaran():
    data_konfirmasi()
    ubah_status()

def data_konfirmasi():    
    os.system("cls")
    print("Pilih data pembayaran yang ingin dikonfirmasi".center(115))
    nomor = 1
    for pembayaran in transaksi.datapembayaran():
        print(f"{nomor}. Nomor Reservasi       : {pembayaran[1]}\n   Waktu pembayaran      : {pembayaran[2]}\n   Nama Pemilik Rekening : {pembayaran[3]}\n   Status Konfirmasi     : {pembayaran[4]}\n")
        nomor += 1
    global pilih_konfirm
    pilih_konfirm = input("Pilih : ")
    while pilih_konfirm.isdigit() == False:
        input("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
        data_konfirmasi()

def ubah_status():
    os.system("cls")
    print(f"Konfirmasi pembayaran nomor {pilih_konfirm}".center(115))
    for pembayaran in transaksi.datapembayaran():
        if pembayaran[1] == int(pilih_konfirm):
            if pembayaran[4] != 'Sudah dikonfirmasi' and pembayaran[4] != 'Pembayaran ditolak':
                pilih_ubah = input("|1| Konfirmasi Pembayaran\n|2| Tolak Pembayaran\nPilih : ")
                while pilih_ubah.isdigit() == False:
                    input("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
                    ubah_status()
                if pilih_ubah == "1":
                    status = "Sudah dikonfirmasi" 
                elif pilih_ubah == "2":
                    status = "Pembayaran ditolak"
                data_ubah_status = {'id' : int(pilih_konfirm), 'status_konfirmasi' : status}
                transaksi.updatestatusbayar(data_ubah_status)
                os.system("cls")
                input(f"Konfirmasi pembayaran nomor {pilih_konfirm} berhasil\nKlik enter untuk lanjut => ".center(115))
                close()
            else:
                print("Maaf. Pembayaran sudah dikonfirmasi".center(115))
                pilih = input("|1| Konfirmasi pembayaran yang lain\n|2| Kembali ke menu utama\n|3| Keluar Aplikasi\nPilih => ")
                if pilih == "1":
                    konfirmasi_pembayaran()
                elif pilih == "2":
                    menuadmin()
                elif pilih == "3":
                    close()
                else:
                    input("Maaf, inputan tidak sesuai. Klik enter untuk lanjut => ".center(115))
                    ubah_status()

def reservasi():
    data_pengantin()
    data_paket()
    data_waktu()
    data_petugas()
    jumlah_undangan()
    admin_bertugas()
    catatan_pengantin()

def data_pengantin():
    os.system("cls")
    print("Masukkan data pengantin dengan benar".center(115))
    global nama_pengantin_pria, nama_pengantin_wanita
    nama_pengantin_pria = input("Nama Pengantin Pria   : ")
    nama_pengantin_wanita = input("Nama Pengantin Wanita : ")

def data_paket():
    global paket_nikah, nama_paket
    os.system("cls")
    print("Pilih paket".center(115))
    for paket in paketnikah.readpaket():
        print(f"{paket[0]}. Paket {paket[3]}\n   Ruangan   : {paket[1]}\n   Fasilitas : {paket[4]}\n   Harga     : {paket[2]}\n")
    pilih_paket = input("Pilih => ")
    while not pilih_paket.isdigit() or int(pilih_paket) not in [paket[0] for paket in paketnikah.readpaket()]:
        input("Maaf, inputan harus berupa angka yang sesuai dengan salah satu paket\nKlik enter untuk lanjut =>".center(115))
        os.system("cls")
        data_paket()
    for paket in paketnikah.readpaket():
        paket_nikah = int(pilih_paket)
        if paket[0] == paket_nikah:
            nama_paket = paket[3]
            break
    print(nama_paket)

def data_waktu():
    global waktu_akad
    os.system("cls")
    print("Pilih waktu pernikahan".center(115))
    tahun = int(input("Tahun (isi menggunakan angka)   : "))
    bulan = int(input("Bulan (isi menggunakan angka)   : "))
    hari = int(input("Tanggal (isi menggunakan angka) : "))
    pilih_hari = datetime(tahun, bulan,hari)
    acara = []
    for day in transaksi.bacareservasi():
        if pilih_hari.date() == day[2].date():
            waktu = day[2].strftime("%H:%M:%S")
            acara.append(waktu)
    jam_akad = ['08:00:00', '10:00:00', '13:00:00']
    nomor = 1
    pilihan_jam = []
    if len(acara) <= 2:
        pilihan_jam = [jam for jam in jam_akad if jam not in acara]
        if pilihan_jam:
                print("Pilihan Jam : ")
                for nomor, jam in enumerate(pilihan_jam, start=1):
                    print(f"  {nomor}. {jam}")
                pilih_jam = input("Pilih => ")
                if pilih_jam.isdigit() and 1 <= int(pilih_jam) <= len(pilihan_jam):
                    jam = pilihan_jam[int(pilih_jam) - 1]
                else:
                    input("Maaf, inputan harus berupa angka. Pilih salah satu jam\nKlik enter untuk lanjut =>".center(115))
                    data_waktu()
                waktu_nikah = datetime.combine(pilih_hari.date(), datetime.strptime(jam, "%H:%M:%S").time())
                waktu_akad = waktu_nikah.strftime("%Y-%m-%d %H:%M:%S")
    else:    
        print("Maaf, jadwal pada hari ini tidak tersedia. Cobalah untuk mengganti hari atau paketnya".center(115))
        pilih_kembali = input("|1| Ganti Paket\n|2| Ganti Tanggal\n|3| Batalkan Reservasi\n Pilih => ")
        if pilih_kembali == "1":
            data_paket()
        elif pilih_kembali == "2":
            data_waktu()
        elif pilih_kembali == "3":
            close()
        else:
            input("Maaf, inputan tidak sesuai. Klik enter untuk lanjut => ")
            data_waktu()

def data_petugas():
    os.system("cls")
    print("Pilih petugas pernikahan".center(115))
    print("-Petugas MC -".center(115))
    nomor = 1
    list_mc = petugasnikah.petugasmc()
    list_hadrah = petugasnikah.petugashadrah()
    list_mubaligh = petugasnikah.petugasmubaligh()
    list_qori = petugasnikah.petugasqori()
    for mc in list_mc:
        print(f"{nomor}. {mc[1]}")
        nomor += 1
    pilih_mc = input("Pilih => ")
    while pilih_mc.isdigit == False or int(pilih_mc) > len(list_mc):
        input("Maaf, inputan harus berupa angka. Pilih salah satu petugas\nKlik enter untuk lanjut => ")
        data_petugas()
    global mc_akad, hadrah_akad, mubaligh_akad, qori_akad
    mc_akad = list_mc[int(pilih_mc) - 1][1]
    os.system("cls")
    print("Pilih petugas pernikahanmu 🤗".center(115))
    print("-Petugas Hadrah -".center(115))
    nomor = 1
    for hadrah in list_hadrah:
        print(f"{nomor}. Tim {hadrah[1]}")
        nomor += 1
    pilih_hadrah = input("Pilih => ")
    while pilih_hadrah.isdigit == False or int(pilih_hadrah) > len(list_hadrah):
        input("Maaf, inputan harus berupa angka. Pilih salah satu petugas\nKlik enter untuk lanjut => ")
        data_petugas()
    hadrah_akad = list_hadrah[int(pilih_hadrah) - 1][1]
    os.system("cls")
    print("Pilih petugas pernikahanmu 🤗".center(115))
    print("-Petugas Mubaligh -".center(115))
    nomor = 1
    for mubaligh in list_mubaligh:
        print(f"{nomor}. {mubaligh[1]}")
        nomor += 1
    pilih_mubaligh = input("Pilih => ")
    while pilih_mubaligh.isdigit == False or int(pilih_mubaligh) > len(list_mubaligh):
        input("Maaf, inputan harus berupa angka. Pilih salah satu petugas\nKlik enter untuk lanjut => ")
        data_petugas()
    mubaligh_akad = list_mubaligh[int(pilih_mubaligh) - 1][1]
    os.system("cls")
    print("Pilih petugas pernikahanmu 🤗".center(115))
    print("-Petugas Qori' -".center(115))
    nomor = 1
    for qori in list_qori:
        print(f"{nomor}. {qori[1]}")
        nomor += 1
    pilih_qori = input("Pilih => ")
    while pilih_qori.isdigit == False or int(pilih_qori) > len(list_qori):
        input("Maaf, inputan harus berupa angka. Pilih salah satu petugas\nKlik enter untuk lanjut => ")
        data_petugas()
    qori_akad = list_qori[int(pilih_qori) - 1][1]

def admin_bertugas():
    global next_admin
    data_admin = admin.readadmin()
    reservasi = transaksi.bacareservasi()
    total_admin = len(data_admin)
    if reservasi:
        last_admin = reservasi[-1][8]
        next_admin = (last_admin % total_admin) + 1
    else:
        next_admin = 1   

def data_pembayaran():
    os.system("cls")
    print("Pembayaran".center(115))
    print("Pembayaran dilakukan pada nomor rekening 012344321 (BCA) an. Yayasan Masjid Jami' Al-Baitul Amien Jember".center(115))
    print("Reservasi tidak akan tersimpan sebelum melakukan transfer\n".center(115))
    for harga in paketnikah.readpaket():
        if harga[0] == paket_nikah:
            print(f"Total Pembayaran : {harga[2]}")
            break
    input("Klik enter apabila pelanggan telah melakukan transfer => ")
    global wkt_tf, pemilik_rek
    wkt_tf = datetime.now()
    waktu_tf = wkt_tf.strftime("%Y-%m-%d %H:%M:%S")
    pemilik_rek = input("Masukkan nama pemilk rekening yang digunakan untuk transfer : ")
    data_pembayaran = {'waktu_pembayaran' : waktu_tf, 'nama_pemilik_rekening' : pemilik_rek, 'status_konfirmasi': 'Belum dikonfirmasi'}
    transaksi.tambahpembayaran(data_pembayaran)
    tambahkanreservasi()

def tambahkanreservasi():
    os.system("cls")
    pembayaran = transaksi.bacapembayaran()
    last_pembayaran = pembayaran[-1][0]
    wkt_reservasi = datetime.now()
    waktu_reservasi = wkt_reservasi.strftime("%Y-%m-%d %H:%M:%S")
    data_reservasi = {'waktu_reservasi': waktu_reservasi, 'waktu_akad_nikah' : waktu_akad, 'catatan_pengantin': catatan_pengantin, 'jumlah_undangan' : undangan_akad, 'nama_pengantin_pria' : nama_pengantin_pria, 'nama_pengantin_wanita' : nama_pengantin_wanita, 'id_paket' : paket_nikah, 'id_admin': next_admin, 'id_pembayaran' : last_pembayaran, 'id_pengguna' : 1}
    transaksi.tambahreservasi(data_reservasi)
    print("Selamat! Reservasi berhasil dilakukan 🙌".center(115))
    input("Klik enter untuk melanjutkan => ")
    close()

def jumlah_undangan():
    os.system("cls")
    global undangan_akad
    print("Jumlah Undangan\n".center(115))
    undangan_akad = input("Masukkan jumlah undangan yang hadir saat acara (Maksimal 100 orang) : ")

def catatan_pengantin():
    os.system("cls")
    print("Catatan Pengantin".center(115))
    print("Isi dengan tanda '-' apabila tidak ingin menambah catatan\n".center(115))
    global catatan_pengantin
    catatan_pengantin = input("Catatan (Contoh: Tolong pakai bunga melati di meja akad): ")
    konfirmasi_reservasi()

def konfirmasi_reservasi():
    os.system("cls")
    print("Konfirmasi reservasi".center(115))
    print(f"Nama pengantin pria        : {nama_pengantin_pria}\nNama Pengantin Wanita      : {nama_pengantin_wanita}\nWaktu akad nikah           : {waktu_akad}\nPaket Pernikahan           : Paket {nama_paket}\nJumlah Undangan            : {undangan_akad}\nCatatan                    : {catatan_pengantin}\nPetugas Pernikahan         : \n  MC         : {mc_akad}\n  Tim Hadrah : {hadrah_akad}\n  Mubaligh   : {mubaligh_akad}\n  Qori'      : {qori_akad}\n")
    pilih_konfirm = input("|1| Konfirmasi Reservasi\n|2| Ganti nama pengantin\n|3| Ganti Paket Pernikahan\n|4| Ganti Waktu Pernikahan\n|5| Ganti Petugas Pernikahan\n|6| Ubah Jumlaah Undangan \n|7| Ubah catatan \n|8| Batalkan Reservasi\nPilih => ")
    if pilih_konfirm == "1":
        data_pembayaran()
    elif pilih_konfirm == "2":
        data_pengantin()
    elif pilih_konfirm == "3":
        data_paket()
    elif pilih_konfirm == "4":
        data_waktu()
    elif pilih_konfirm == "5":
        data_petugas()
    elif pilih_konfirm == "6":
        jumlah_undangan()
    elif pilih_konfirm == "7":
        catatan_pengantin()
        pass
    elif pilih_konfirm == "8":
        close()
    else: 
        input("Maaf, inputan tidak valid. Klik enter untuk lanjut => ")
        konfirmasi_reservasi()

def lihatjadwal():
    os.system("cls")
    print("Jadwal Pernikahan".center(115))
    reservations_by_date = {}
    def date_to_key(date):
        return date.strftime("%Y-%m-%d")
    today = datetime.today().date()
    tomorrow = today + timedelta(days=1)
    for reservasi in transaksi.riwayatreservasi():
        reservation_date = reservasi[2].date()
        key = date_to_key(reservation_date)
        if key not in reservations_by_date:
            reservations_by_date[key] = []
        reservations_by_date[key].append(reservasi)
    nomor = 1
    today_key = date_to_key(today)
    if today_key in reservations_by_date:
        print("\nPernikahan Hari Ini".center(115))
        for reservasi in reservations_by_date[today_key]:
            print(f"{nomor}. Nomor Reservasi   : {reservasi[0]}\n   Pengantin         : {reservasi[5]}  \n   Waktu             : {reservasi[2]}\n   Nama Paket        : Paket {reservasi[6]}\n   Status Pembayaran : {reservasi[8]}\n   Jumlah Undangan   : {reservasi[4]}\n   Catatan           : {reservasi[3]}")
            nomor += 1
    else:
        print("\nTidak ada pernikahan hari ini".center(115))
    tomorrow_key = date_to_key(tomorrow)
    if tomorrow_key in reservations_by_date:
        print("\nPernikahan Besok".center(115))
        for reservasi in reservations_by_date[tomorrow_key]:
            print(f"{nomor}. Nomor Reservasi   : {reservasi[0]}\n   Pengantin         : {reservasi[5]}  \n   Waktu             : {reservasi[2]}\n   Nama Paket        : Paket {reservasi[6]}\n   Status Pembayaran : {reservasi[8]}\n   Jumlah Undangan   : {reservasi[4]}\n   Catatan           : {reservasi[3]}")
    else:
        print("\nTidak ada pernikahan besok".center(115))
    pilih_menu = input("|1| Kembali ke menu utama\n|2| Keluar dari aplikasi\nPilih=> ")
    if pilih_menu == "1":
        menuadmin() 
    elif pilih_menu =="2":
        close() 
    else:
        input("Maaf, inputan tidak valid. Klik enter untuk lanjut => ")
        lihatjadwal()

def caririwayatreservasi():
    os.system("cls")
    print("Cari Riwayat Reservasi".center(115))
    reservasi = transaksi.reservasiterurut()  
    n = len(reservasi)
    step = int(n ** 0.5)
    prev = 0
    nomor = 1
    pilih_cari = input("|1| Cari berdasarkan tanggal pernikahan \n|2| Cari berdasarkan nomor reservasi\nPilih => ")
    os.system("cls")
    print("Masukkan spesifikasi data yang dicari".center(115))
    if pilih_cari == "1":    
        data_cari = 2
        tahun = int(input("Tahun (isi menggunakan angka)   : "))
        bulan = int(input("Bulan (isi menggunakan angka)   : "))
        hari = int(input("Tanggal (isi menggunakan angka) : "))
        target = datetime(tahun,bulan,hari).date()
        reservasi = transaksi.reservasiterurut()  
        while prev < n and reservasi[min(step, n) - 1][data_cari].date() < target:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                print("Data tidak ditemukan")
        while prev < min(step, n) and reservasi[prev][data_cari].date() < target:
            prev += 1
            if prev == min(step, n):
                print("Data tidak ditemukan")
        if prev < n and reservasi[prev][data_cari].date() == target:
            os.system("cls")
            print("Hasil Pencarian".center(115))
            start = prev
            while start >= 0 and reservasi[start][data_cari].date() == target:
                start -= 1
            start += 1
            end = prev
            while end < n and reservasi[end][data_cari].date() == target:
                end += 1
            for i in range(start, end):
                print(f"{nomor}. Nomor Reservasi   : {reservasi[i][0]}\n   Pengantin         : {reservasi[i][5]}  \n   Waktu             : {reservasi[i][2]}\n   Nama Paket        : Paket {reservasi[i][6]}\n   Status Pembayaran : {reservasi[i][8]}\n   Jumlah Undangan   : {reservasi[i][4]}\n   Catatan           : {reservasi[i][3]}")
                nomor += 1
        else:
            os.system("cls")
            print("Data tidak ditemukan".center(115))
    elif pilih_cari == "2":
        reservasi = transaksi.riwayatreservasi()
        data_dicari = input("Nomor reservasi : ")
        target = int(data_dicari)
        while prev < n and reservasi[min(step, n) - 1][0] < target:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                print("Data tidak ditemukan")
        while prev < min(step, n) and reservasi[prev][0] < target:
            prev += 1
            if prev == min(step, n):
                print("Data tidak ditemukan")
        if prev < n and reservasi[prev][0] == target:
            os.system("cls")
            print("Hasil Pencarian".center(115))
            print(f"Nomor Reservasi   : {reservasi[prev][0]}\n   Pengantin         : {reservasi[prev][5]}  \n   Waktu             : {reservasi[prev][2]}\n   Nama Paket        : Paket {reservasi[prev][6]}\n   Status Pembayaran : {reservasi[prev][8]}\n   Jumlah Undangan   : {reservasi[prev][4]}\n   Catatan           : {reservasi[prev][3]}")
        else:
            os.system("cls")
            print("Data tidak ditemukan".center(115))
    else:
        input("Maaf, inputan tidak valid. Klik enter untuk lanjut => ")
        caririwayatreservasi()
    
    pilih_menu = input("|1| Kembali ke menu utama\n|2| Keluar dari aplikasi\nPilih=> ")
    if pilih_menu == "1":
        menuadmin() 
    elif pilih_menu == "2":
        close() 
    else:
        input("Maaf, inputan tidak valid. Klik enter untuk lanjut => ")
        caririwayatreservasi()

def close():
    os.system("cls")
    print("Apakah kamu ingin keluar dari aplikasi?\n".center(115))
    pilih_close = input("|1| Ya\n|2| Tidak, kembali ke menu utama\nPilih: ")
    while pilih_close.isdigit() == False:
        os.system("cls")
        print("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>\n".center(115))
        pilih_close = input("|1| Ya\n|2| Tidak, kembali ke menu utama\nPilih: ")
    if pilih_close == "1":
        os.system("cls")
        print("Terima kasih telah menggunakan aplikasi NikMate. See You 👋".center(115))
    elif pilih_close == "2":
        menuadmin()

login()