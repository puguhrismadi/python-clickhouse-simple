```markdown
# 📊 Belajar ClickHouse: Aplikasi CLI Python

Proyek ini adalah aplikasi Python sederhana berbasis CLI untuk belajar cara menggunakan 
ClickHouse secara efisien menggunakan Python. Data awal disimpan dalam format **Parquet** 
dan dimuat ke dalam **ClickHouse**. 
Aplikasi ini memiliki fitur query interaktif menggunakan **menu berbasis teks**.

---

## ✅ Fitur Aplikasi

=== Menu CLI ClickHouse ===
1. Hitung total record
2. Cari data berdasarkan location
3. Tampilkan data 100 baris dengan navigasi
0. Keluar
```
## ✅ Rekomendasi

Gunakan **ClickHouse** jika:
- ✅ Data Anda besar (ratusan MB sampai TB)
- ✅ Perlu performa query tinggi
- ✅ Akan sering menjalankan query OLAP
- ✅ Membutuhkan sistem produksi yang scalable

Gunakan **Parquet langsung** jika:
- ⚠️ Hanya eksplorasi data ringan atau ad-hoc
- ⚠️ Tidak ingin repot setup database
 
### Contoh Output:

```
Pilih menu: 1
✅ Jumlah total record: 100.000.000 (seratus juta baris) data
🕒 Lama eksekusi: 3.26 ms
```

---

## 🧰 Kebutuhan Sistem

- Python 3.8+
- ClickHouse (dapat dijalankan via Docker)
- Library Python:
  - `clickhouse-connect`
  - `pandas`

---

## 🚀 Cara Menjalankan

1. **Clone repositori dan masuk ke direktori proyek**:
   ```bash
   git clone https://github.com/puguhrismadi/belajar-clickhouse.git
   cd belajar-clickhouse
   ```

2. **(Opsional) Buat virtual environment**:
   ```bash
   python -m venv clickvenv
   source clickvenv/bin/activate
   ```

3. **Install dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Pastikan ClickHouse berjalan**, misal via Docker:
   ```bash
   docker run -d --name clickhouse-server -p 8123:8123 -p 9000:9000 clickhouse/clickhouse-server
   ```

5. **Jalankan loader untuk memuat data dari file Parquet ke ClickHouse**:
   ```bash
   python load_parquete_to_clickhouse.py
   ```

6. **Jalankan aplikasi CLI**:
   ```bash
   python cli_clickhouse.py
   ```

---

## 📂 Struktur File

```
.
├── dataset_pd.parquet              # Dataset awal (Parquet)
├── load_parquete_to_clickhouse.py # Loader dari Parquet ke ClickHouse
├── main.py              # Aplikasi CLI utama
├── requirements.txt               # Dependensi Python
├── query_clickhouse.py               #sample query ke database clickhouse
└── README.md                      # Dokumentasi proyek
```

---

## ⚠️ Catatan Tambahan
- Datafile(100juta row) parquete di generate dari link : Clone Official 1 Billion Row Challenge [repo](https://github.com/gunnarmorling/1brc)
- Pastikan user ClickHouse (`myuser`) memiliki hak akses: `SELECT`, `CREATE`, dan `INSERT`.
- Anda dapat menyesuaikan kolom dataset (misalnya `location`, `temperature`) di dalam skrip Python.
- Ganti konfigurasi koneksi di file Python sesuai dengan kredensial dan port server ClickHouse Anda.

---

## 📜 Lisensi

Proyek ini dilisensikan dengan [MIT License](https://opensource.org/licenses/MIT) – bebas digunakan untuk belajar dan pengembangan pribadi.
```
