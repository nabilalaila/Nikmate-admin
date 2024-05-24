import psycopg2

def datapembayaran():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT p.id_pembayaran, r.id_reservasi, p.waktu_pembayaran, p.nama_pemilik_rekening, p.status_konfirmasi from reservasi r join pembayaran p on p.id_pembayaran = r.id_pembayaran order by r.id_reservasi"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def bacapembayaran():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT * from pembayaran"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def updatestatusbayar(request):
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = f"UPDATE pembayaran SET status_konfirmasi = '{request['status_konfirmasi']}' where id_pembayaran = {request['id']};"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def bacareservasi():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT * from reservasi"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def tambahpembayaran(request):
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = f"INSERT INTO pembayaran (waktu_pembayaran, nama_pemilik_rekening, status_konfirmasi) VALUES ('{request['waktu_pembayaran']}', '{request['nama_pemilik_rekening']}', '{request['status_konfirmasi']}')"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def tambahreservasi(request):
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = f"INSERT INTO reservasi(waktu_reservasi, waktu_akad_nikah, catatan_pengantin, jumlah_undangan, nama_pengantin_pria, nama_pengantin_wanita, id_paket, id_admin, id_pembayaran, id_pengguna) VALUES  ('{request['waktu_reservasi']}', '{request['waktu_akad_nikah']}', '{request['catatan_pengantin']}', '{request['jumlah_undangan']}', '{request['nama_pengantin_pria']}', '{request['nama_pengantin_wanita']}', '{request['id_paket']}', '{request['id_admin']}', '{request['id_pembayaran']}', '{request['id_pengguna']}')"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def riwayatreservasi():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = """select r.id_reservasi, r.waktu_reservasi, r.waktu_akad_nikah, r.catatan_pengantin, r.jumlah_undangan, r.nama_pengantin_pria ||' dan '|| r.nama_pengantin_wanita,
p.nama_paket, a.nama_admin, s.status_konfirmasi, pe.username_pengguna
from reservasi r
join paket_reservasi p on p.id_paket = r.id_paket
join admin a on a.id_admin = r.id_admin
join pembayaran s on s.id_pembayaran = r.id_pembayaran
join pengguna pe on pe.id_pengguna = r.id_pengguna order by r.id_reservasi"""
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def reservasiterurut():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = """select r.id_reservasi, r.waktu_reservasi, r.waktu_akad_nikah, r.catatan_pengantin, r.jumlah_undangan, r.nama_pengantin_pria ||' dan '|| r.nama_pengantin_wanita,
p.nama_paket, a.nama_admin, s.status_konfirmasi, pe.username_pengguna
from reservasi r
join paket_reservasi p on p.id_paket = r.id_paket
join admin a on a.id_admin = r.id_admin
join pembayaran s on s.id_pembayaran = r.id_pembayaran
join pengguna pe on pe.id_pengguna = r.id_pengguna order by r.waktu_akad_nikah"""
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data