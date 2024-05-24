import psycopg2
from collections import defaultdict

def readpaket():
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="Gwbis@99", host="localhost", port="5433")
    cur = conn.cursor()
    sql = """
    SELECT p.id_paket, p.nama_paket, f.nama_fasilitas, r.nama_ruangan, p.harga_paket 
FROM detail_fasilitas_paket d 
JOIN fasilitas f ON f.id_fasilitas = d.id_fasilitas
JOIN paket_reservasi p ON p.id_paket = d.id_paket
JOIN ruangan r ON r.id_ruangan = p.id_ruangan
order by id_paket
    """    
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    paket_dict = {}

    for id_paket, nama_paket, nama_fasilitas, nama_ruangan, harga_paket in data:
        if id_paket not in paket_dict:
            paket_dict[id_paket] = {
                "nama_paket": nama_paket,
                "fasilitas": set(),
                "nama_ruangan": nama_ruangan,
                "harga_paket": harga_paket
            }
        paket_dict[id_paket]["fasilitas"].add(nama_fasilitas)
    
    result = []
    for id_paket, paket_info in paket_dict.items():
        result.append((id_paket, paket_info['nama_ruangan'], paket_info['harga_paket'], paket_info['nama_paket'], ', '.join(paket_info['fasilitas'])))
    return result

