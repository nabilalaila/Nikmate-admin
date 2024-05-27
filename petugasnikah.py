import psycopg2

def readpetugas():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT p.id_petugas_pernikahan, p.nama_petugas, p.telp_petugas, p.honorarium_petugas, j.jenis_petugas from petugas_pernikahan p join jenis_petugas j on (j.id_jenis_petugas = p.id_jenis_petugas)"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def writepetugas(request):
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = f"INSERT INTO petugas_pernikahan(nama_petugas, telp_petugas, honorarium_petugas, id_jenis_petugas) VALUES  ('{request['nama_petugas']}', '{request['no_telp']}',  '{request['Honorarium']}', '{request['jenis_petugas']}')"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def deletepetugas(request):
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = f"DELETE FROM petugas_pernikahan WHERE id_petugas_pernikahan = {request['id']};"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def updatepetugas(request):
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = f"UPDATE petugas_pernikahan SET nama_petugas = '{request['nama_petugas']}', telp_petugas = '{request['no_telp']}', honorarium_petugas = '{request['Honorarium']}', id_jenis_petugas= '{request['jenis_petugas']}' where id_petugas_pernikahan = {request['id']};"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def petugasmc():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT p.id_petugas_pernikahan, p.nama_petugas, p.telp_petugas, p.honorarium_petugas, j.jenis_petugas from petugas_pernikahan p join jenis_petugas j on (j.id_jenis_petugas = p.id_jenis_petugas) WHERE j.jenis_petugas = 'MC'"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def petugashadrah():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT p.id_petugas_pernikahan, p.nama_petugas, p.telp_petugas, p.honorarium_petugas, j.jenis_petugas from petugas_pernikahan p join jenis_petugas j on (j.id_jenis_petugas = p.id_jenis_petugas) WHERE j.jenis_petugas = 'Tim Hadrah'"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def petugasmubaligh():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT p.id_petugas_pernikahan, p.nama_petugas, p.telp_petugas, p.honorarium_petugas, j.jenis_petugas from petugas_pernikahan p join jenis_petugas j on (j.id_jenis_petugas = p.id_jenis_petugas) WHERE j.jenis_petugas = 'Mubaligh'"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def petugasqori():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT p.id_petugas_pernikahan, p.nama_petugas, p.telp_petugas, p.honorarium_petugas, j.jenis_petugas from petugas_pernikahan p join jenis_petugas j on (j.id_jenis_petugas = p.id_jenis_petugas) WHERE j.jenis_petugas = 'Qori'"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def tambahkedetail(request):
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = f"INSERT INTO detail_petugas(id_reservasi, id_petugas_pernikahan) VALUES  ({request['id_reservasi']}, {request['id_petugas']})"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def panggilidpetugas(request):
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = f"SELECT id_petugas_pernikahan FROM (SELECT p.id_petugas_pernikahan, p.nama_petugas, j.jenis_petugas, ROW_NUMBER() OVER (PARTITION BY jenis_petugas ORDER BY id_petugas_pernikahan) AS row_num FROM petugas_pernikahan p join jenis_petugas j on j.id_jenis_petugas = p.id_jenis_petugas ) AS subquery WHERE jenis_petugas = '{request['jenis_petugas']}'AND row_num = {request['id_sekarang']};"
    cur.execute(sql)
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data[0]

def detailpetugas(request):
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = f"""SELECT p.nama_petugas
from detail_petugas dp 
join petugas_pernikahan p on p.id_petugas_pernikahan = dp.id_petugas_pernikahan
join reservasi r on r.id_reservasi = dp.id_reservasi
join jenis_petugas j on (j.id_jenis_petugas = p.id_jenis_petugas)
where r.id_reservasi = {request['id_reservasi']} and j.jenis_petugas = '{request['jenis_petugas']}'
order by r.id_reservasi"""
    cur.execute(sql)
    data = cur.fetchone()
    cur.close()
    conn.close()
    if data : 
        return data[0]
    else:
        return "Petugas sudah tidak tersedia. Harap cari pengganti"
       

