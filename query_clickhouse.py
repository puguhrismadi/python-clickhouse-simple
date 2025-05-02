import clickhouse_connect
import pandas as pd

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

# Contoh query OLAP cepat
query = """
SELECT location, COUNT(*) AS jumlah, AVG(temperature) AS rata_rata 
FROM dataset_pd 
GROUP BY location 
ORDER BY jumlah DESC 
LIMIT 10
"""

result = client.query_df(query)
print(result)
