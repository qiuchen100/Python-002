import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 8889,
    'user': 'root',
    'password': 'root',
    'db': 'py_xly',
    'charset': 'utf8mb4'
}

if __name__ == "__main__":
    conn = pymysql.connect(**dbInfo)
    cur = conn.cursor()
    try:
        values = [(id, str(id)+'test') for id in range(20)]
        cnt = cur.executemany('insert into test_tb values (%s, %s)', values)
        print(cnt)
        cur.close()
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:

        conn.close()
