import pandas as pd
import clickhouse_connect
import os
import sys

# Konfigurasi
parquet_path = 'dataset_pd.parquet'
table_name = 'dataset_pd'

# Cek file Parquet
if not os.path.exists(parquet_path):
    print(f"❌ File tidak ditemukan: {parquet_path}")
    sys.exit(1)

# Load Parquet ke DataFrame
try:
    df = pd.read_parquet(parquet_path)
    print(f"✅ File '{parquet_path}' berhasil dimuat. Jumlah baris: {len(df)}, Kolom: {list(df.columns)}")
except Exception as e:
    print(f"❌ Gagal membaca file Parquet: {e}")
    sys.exit(1)

# Koneksi ke ClickHouse
try:
    client = clickhouse_connect.get_client(
        host='localhost',
        port=8123,
        username='myuser',
        password='mypassword'
    )
    print("✅ Terhubung ke ClickHouse.")
except Exception as e:
    print(f"❌ Gagal koneksi ke ClickHouse: {e}")
    sys.exit(1)

# Mapping tipe data pandas → ClickHouse
def map_dtype(dtype):
    dtype = str(dtype)
    if dtype == 'object':
        return 'String'
    elif dtype.startswith('float'):
        return 'Float64'
    elif dtype.startswith('int'):
        return 'Int64'
    elif dtype == 'bool':
        return 'UInt8'
    elif 'datetime' in dtype:
        return 'DateTime64(3)'  # presisi 3 digit
    else:
        return 'String'  # fallback default

# Generate definisi kolom untuk CREATE TABLE
columns = ',\n    '.join(
    f"{col} {map_dtype(dtype)}" for col, dtype in zip(df.columns, df.dtypes)
)

# Drop dan buat ulang tabel
try:
    client.command(f"DROP TABLE IF EXISTS {table_name}")
    client.command(f"""
    CREATE TABLE {table_name} (
        {columns}
    ) ENGINE = MergeTree()
    ORDER BY tuple()
    """)
    print(f"✅ Tabel '{table_name}' berhasil dibuat.")
except Exception as e:
    print(f"❌ Gagal membuat tabel: {e}")
    sys.exit(1)

# Insert data ke ClickHouse
try:
    client.insert_df(table_name, df)
    print("✅ Data berhasil di-insert ke ClickHouse.")
except Exception as e:
    print(f"❌ Gagal insert data: {e}")
    sys.exit(1)
