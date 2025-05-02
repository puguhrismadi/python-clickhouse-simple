import clickhouse_connect
import time
import sys

# Inisialisasi koneksi ke ClickHouse
try:
    client = clickhouse_connect.get_client(
        host='localhost',
        port=8123,
        username='myuser',     # Ganti jika perlu
        password='mypassword'  # Ganti jika perlu
    )
except Exception as e:
    print(f"❌ Gagal koneksi ke ClickHouse: {e}")
    sys.exit(1)

def count_records():
    start_time = time.time()
    result = client.query("SELECT COUNT(*) FROM dataset_pd")
    duration = (time.time() - start_time) * 1000  # ms
    print(f"✅ Jumlah total record: {result.result_rows[0][0]}")
    print(f"🕒 Lama eksekusi: {duration:.2f} ms")

def search_by_location(location_name):
    start_time = time.time()
    query = """
    SELECT * FROM dataset_pd
    WHERE location = %(location)s
    LIMIT 100
    """
    result = client.query(query, parameters={'location': location_name})
    duration = (time.time() - start_time) * 1000
    if result.result_rows:
        print(f"✅ Ditemukan {len(result.result_rows)} record untuk location '{location_name}':")
        for row in result.result_rows:
            print(row)
    else:
        print(f"⚠️ Tidak ada data ditemukan untuk location '{location_name}'")
    print(f"🕒 Lama eksekusi: {duration:.2f} ms")

def browse_data():
    offset = 0
    page_size = 100
    total_rows = client.query("SELECT COUNT(*) FROM dataset_pd").result_rows[0][0]

    while True:
        query = f"SELECT * FROM dataset_pd LIMIT {page_size} OFFSET {offset}"
        start_time = time.time()
        result = client.query(query)
        duration = (time.time() - start_time) * 1000

        if not result.result_rows:
            print("⚠️ Tidak ada data di halaman ini.")
        else:
            print(f"\n📄 Menampilkan data dari baris {offset + 1} sampai {offset + len(result.result_rows)}:")
            for row in result.result_rows:
                print(row)
            print(f"🕒 Lama eksekusi: {duration:.2f} ms")

        print("\n[n] Berikutnya | [p] Sebelumnya | [q] Kembali ke menu")
        nav = input("Pilih aksi: ").lower()

        if nav == 'n':
            if offset + page_size < total_rows:
                offset += page_size
            else:
                print("📍 Sudah di akhir data.")
        elif nav == 'p':
            if offset - page_size >= 0:
                offset -= page_size
            else:
                print("📍 Sudah di awal data.")
        elif nav == 'q':
            break
        else:
            print("❌ Input tidak valid.")

def menu():
    while True:
        print("\n=== Menu CLI ClickHouse ===")
        print("1. Hitung total record")
        print("2. Cari data berdasarkan location")
        print("3. Tampilkan data 100 baris dengan navigasi")
        print("0. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            count_records()
        elif choice == '2':
            loc = input("Masukkan nama location: ")
            search_by_location(loc)
        elif choice == '3':
            browse_data()
        elif choice == '0':
            print("👋 Keluar dari program.")
            break
        else:
            print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
