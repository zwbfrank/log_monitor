import pymysql

def pymysql_conn():
    # databases config
    config = {
        'db': 'log_DB',
        'user': 'root',
        'password': 'password',
        'host': '127.0.0.1',
        'port': 3306,
        'charset': 'utf8',
    }
    try:
        conn = pymysql.connect(**config)
    except:
        print("Cannot connect into database.")
    
    # cursor = conn.cursor()
    return conn


def get_log_path_data():
    conn = pymysql_conn()
    cursor = conn.cursor()
    sql = 'select *from log_analyze_logmonitor'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
data = get_log_path_data()
log_path = data[2][2]
log_type = data[2][1]
local_newest_files = []
ssh_newest_files = []

