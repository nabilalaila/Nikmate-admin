import psycopg2

def readadmin():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT nama_admin, password_admin from admin"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def readcust():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT username_pengguna, nama_lengkap_pengguna, password_pengguna, email_pengguna, telp_pengguna, id_pengguna from pengguna"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def writecust(request):
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = f"INSERT INTO pengguna (username_pengguna, nama_lengkap_pengguna, password_pengguna, email_pengguna, telp_pengguna) VALUES ('{request['username']}', '{request['nama_pengguna']}',  '{request['password']}', '{request['email']}', '{request['no_telp']}')"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()