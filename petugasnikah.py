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
