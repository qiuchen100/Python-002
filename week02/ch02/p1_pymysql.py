import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 8889,
    'user': 'root',
    'password': 'root',
    'db': 'py_xly',
    'charset': 'utf8mb4'
}

sqls = ['select 1', 'select VERSION()', 'show databases']

results = []


class ConnDB(object):

    def __init__(self, dbInfo, sqls):
        # self.host = dbInfo['host']
        # self.port = dbInfo['port']
        # self.user = dbInfo['user']
        # self.password = dbInfo['password']
        # self.db = dbInfo['db']
        self.dbInfo = dbInfo
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(**dbInfo)
        with conn.cursor() as cur:
            for sql in self.sqls:
                cnt = cur.execute(sql)
                results.append(cur.fetchone())
                print(f'sql: {sql} | 查询到{cnt}行数。')
        conn.close()


if __name__ == "__main__":
    conn = ConnDB(dbInfo, sqls)
    conn.run()
    print(results)
