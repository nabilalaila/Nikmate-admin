CREATE TABLE ruangan (
    id_ruangan       SMALLSERIAL  PRIMARY KEY NOT NULL,
    nama_ruangan VARCHAR(50) NOT NULL
);

CREATE TABLE fasilitas (
    id_fasilitas      SMALLSERIAL PRIMARY KEY NOT NULL,
    nama_fasilitas VARCHAR(50) NOT NULL
);

CREATE TABLE admin (
    id_admin           SMALLSERIAL PRIMARY KEY NOT NULL,
    nama_admin     VARCHAR(50) NOT NULL,
    telp_admin        VARCHAR(12) UNIQUE NOT NULL,
    email_admin     VARCHAR(320) UNIQUE NOT NULL,
    password_admin CHAR(8) NOT NULL
);

CREATE TABLE pengguna (
    id_pengguna                       SMALLSERIAL PRIMARY KEY NOT NULL,
    username_pengguna         VARCHAR(20) UNIQUE NOT NULL,
    nama_lengkap_pengguna VARCHAR(50) NOT NULL,
    password_pengguna         CHAR(8) NOT NULL,
    email_pengguna               VARCHAR(320) UNIQUE NOT NULL,
    telp_pengguna         VARCHAR(12) UNIQUE NOT NULL
);

CREATE TABLE jenis_petugas (
    id_jenis_petugas  SMALLSERIAL PRIMARY KEY NOT NULL,
    jenis_petugas      VARCHAR(20) NOT NULL
);

CREATE TABLE paket_reservasi (
    id_paket              SMALLSERIAL PRIMARY KEY NOT NULL,
    nama_paket        VARCHAR(50) NOT NULL,
    harga_paket        INTEGER NOT NULL,
    id_ruangan 	   SMALLINT NOT NULL,
	FOREIGN KEY (id_ruangan) REFERENCES ruangan(id_ruangan)
);

CREATE TABLE pembayaran (
    id_pembayaran                 SMALLSERIAL PRIMARY KEY NOT NULL,
    waktu_pembayaran         TIMESTAMP NOT NULL,
    nama_pemilik_rekening  VARCHAR(50) NOT NULL,
    status_konfirmasi         VARCHAR(20) NOT NULL 
);

CREATE TABLE reservasi (
    id_reservasi                    SMALLSERIAL NOT NULL PRIMARY KEY,
    waktu_reservasi             TIMESTAMP NOT NULL,
    waktu_akad_nikah         TIMESTAMP NOT NULL,
    catatan_pengantin          TEXT,
    jumlah_undangan           INTEGER NOT NULL,
    nama_pengantin_pria     VARCHAR(50) NOT NULL,
    nama_pengantin_wanita VARCHAR(50) NOT NULL,
	id_paket 		   SMALLINT NOT NULL,
	id_admin		   SMALLINT NOT NULL,
	id_pembayaran	   SMALLINT NOT NULL,
	id_pengguna 		   SMALLINT NOT NULL,
	FOREIGN KEY (id_paket) REFERENCES paket_reservasi(id_paket),
	FOREIGN KEY (id_admin) REFERENCES admin(id_admin),
	FOREIGN KEY (id_pembayaran) REFERENCES pembayaran(id_pembayaran),
	FOREIGN KEY (id_pengguna) REFERENCES pengguna(id_pengguna)
);

CREATE TABLE petugas_pernikahan (
    id_petugas_pernikahan           SMALLSERIAL PRIMARY KEY NOT NULL,
    nama_petugas                        VARCHAR(50) NOT NULL,
    telp_petugas                           VARCHAR(12) NOT NULL,
    honorarium_petugas              INTEGER NOT NULL,
    id_jenis_petugas                    SMALLINT NOT NULL,
	FOREIGN KEY (id_jenis_petugas) REFERENCES jenis_petugas(id_jenis_petugas)
);

CREATE TABLE detail_petugas (
    id_reservasi       			  SMALLSERIAL NOT NULL, 
    id_petugas_pernikahan 		  SMALLINT NOT NULL,
	FOREIGN KEY (id_reservasi) REFERENCES reservasi(id_reservasi),
	FOREIGN KEY (id_petugas_pernikahan) REFERENCES petugas_pernikahan(id_petugas_pernikahan),
	PRIMARY KEY (id_reservasi, id_petugas_pernikahan)
);

CREATE TABLE detail_fasilitas_paket (
    id_fasilitas   	      SMALLINT NOT NULL,
    id_paket                 SMALLINT NOT NULL,
	FOREIGN KEY (id_fasilitas) REFERENCES fasilitas(id_fasilitas),
	FOREIGN KEY (id_paket) REFERENCES paket_reservasi(id_paket),
	PRIMARY KEY (id_fasilitas, id_paket)
);

INSERT INTO ruangan(nama_ruangan)
VALUES ('Kubah Utama'), ('Kubah Utara'), ('Kubah Selatan');

INSERT INTO fasilitas (nama_fasilitas)
VALUES ('Meja Tamu'), ('Meja Ijab Kabul'), ('AC'), ('Sound system'), ('Dokumentasi akad nikah by Alba Media'), ('Banner dan papan latar'), 
('Ruang tunggu pengantin'), ('Dekorasi full bunga'), ('Buku Tamu'), ('Hampers Bimbingan Pernikahan'), ('Buket Bunga');

admin
INSERT INTO admin(nama_admin, telp_admin, email_admin, password_admin)
VALUES ('Nuriyah Aliyana', '086545983256', 'nuriyahal@gmail.com', 'Ajhwes76'), 
('Fadlan Arsaka', '086578952357', 'fadlanaa546@gmail.com','f@dl4n98'),
('Liliyana Gilang','085641783254','liliyann@gmail.com','g1Lang//');

INSERT INTO pengguna(username_pengguna, nama_lengkap_pengguna, password_pengguna, email_pengguna, telp_pengguna)
VALUES ('Dwiindi', 'Dwi Indira Sari', 'Indd43*', 'dwiindira@gmail.com', '086572490567'), 
('Zidanaf', 'Zidan Afganesta Putra', 'Jid4n&', 'zidannaf@gmail,com', '084530564961'),
('Riskaftria', 'Riska Nuriyah Fitria', '030599', 'riskanurr@gmail.com', '032715863815'),
('Anandadiafa','Ananda Diafa','Diaff@8', 'anandadiafa23@gmail.com', '084528941351'),
('Rioperdana', 'Rio Azkana Perdana', 'perd@@n7', 'rioperdana@gmail.com', '083579410235')

INSERT INTO jenis_petugas(jenis_petugas)
VALUES ('MC'), ('Tim Hadrah'), ('Qori'), ('Mubaligh')

INSERT INTO paket_reservasi (nama_paket, harga_paket, id_ruangan)
VALUES ('Makkah', 5000000, 1), 
('Madinah', 4500000, 2),
('Arafah', 4500000, 3),
('Mina', 7000000, 1),
('Rahmah', 6500000, 2),
('Nabawi', 6500000, 3);

INSERT INTO pembayaran(waktu_pembayaran, nama_pemilik_rekening, status_konfirmasi)
VALUES ('2024-05-14 00:00:00', 'Nazida Fatma', 'Sudah dikonfirmasi'), 
('2024-05-14 14:05:17', 'Zidan Afganesta Putra', 'Sudah dikonfirmasi'),
('2024-05-15 08:01:50', 'Riska Nuriyah Fitria', 'Pembayaran ditolak'),
('2024-05-15 10:40:09', 'Ananda Diafa', 'Sudah dikonfirmasi'),
('2024-05-15 16:17:18', 'Rio Azkana Perdana', 'Belum dikonfirmasi')

INSERT INTO reservasi(waktu_reservasi, waktu_akad_nikah, catatan_pengantin, jumlah_undangan, nama_pengantin_pria, nama_pengantin_wanita, id_paket, id_admin, id_pembayaran, id_pengguna)
VALUES ('2024-05-13 23:10:20', '2024-09-14 08:00:00', '-', 56, 'Azka Mazaya', 'Nazida Fatma', 4, 1, 1, 1), 
('2024-05-15 06:19:20', '2024-10-19 08:00:00', 'Apabila berkenan mohon disiapkan karpet khusus untuk ibu saya yang memakai kursi roda supaya tidak najis', 30, 'Zidan Afganesta Putra', 'Rina Amalana', 4, 2, 2, 2),
('2024-05-15 06:16:20', '2024-10-15 10:00:00', '-', 33, 'Ahmad Annahid', 'Riska Nuriyah Fitria', 1, 3, 3, 3),
('2024-05-15 08:18:45', '2024-12-02 08:00:00', 'Rombongan akan datang pukul 8, pengantin datang pukul setengah 9', 24, 'Ananda Diafa', 'Meira Natasya', 2, 1, 4, 4),
('2024-05-15 14:07:08', '2024-09-20 08:00:00', '-', 30, 'Rio Azkana Perdana', 'Nanda Avasya Riana', 4, 2, 5, 5);

INSERT INTO petugas_pernikahan(nama_petugas, telp_petugas, honorarium_petugas, id_jenis_petugas)
VALUES ('H. Ahmad Nasruddin', '086467246486', 1000000, 4),
('Rama Airuddin', '084621793524', 300000, 3),
('Arya Hasanauddin', '086574123658', 250000, 1),
('Nurul Musthofa', '086569614865', 500000, 2),
('Rizky Pratama', '081234567890', 300000, 1),
('Fajar Ahmad Setiawan', '085612345678', 300000, 3),
('H. Irfan Muhammad', '082345678901', 1500000, 4),
('Lubabul qulub', '083487945145', 700000, 2)

INSERT INTO detail_petugas(id_reservasi, id_petugas_pernikahan)
VALUES (1,1), (1,2), (1,3), (1,4), (2,7), (2,8), (2,2), (2,5), (3,3), (3,4), (3,6), (3,1), (4,5), (4,8), (4,2), (4,7), (5,3), (5,4), (5,6), (5,1)

INSERT INTO detail_fasilitas_paket(id_fasilitas, id_paket)
VALUES (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (1,4), (2,4), (3,4), (4,4), (5,4), (7,4), (8,4), (9,4), (10,4), (11,4),
(1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (1,5), (2,5), (3,5), (4,5), (5,5), (7,5), (8,5), (9,5), (10,5), (11,5)
