import pymysql
pymysql.install_as_MySQLdb()
# from datetime import time, datetime, timedelta
# import datetime


tables = ['log_analyze_adminweberror',
          'log_analyze_alibblifeweberror',
          'log_analyze_bizserviceerror',
          'log_analyze_alilifeserviceerror',
          'log_analyze_communicationserviceerror',
          'log_analyze_configserviceerror',
          'log_analyze_mobileweberror',
          'log_analyze_orderserviceerror',
          'log_analyze_payserviceerror',
          'log_analyze_promotionserviceerror',
          'log_analyze_shopserviceerror',
          'log_analyze_userserviceerror',
          'log_analyze_wapweberror',
          'log_analyze_wxserviceerror',
          'log_analyze_remotebizinfo94',
          'log_analyze_remotebizerror94',
          'log_analyze_remotebizinfo98',
          'log_analyze_remotebizerror98',]

def pymysql_conn():
    # databases config
    config = {
        'db': 'log_monitor',
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

def truncate(table):
    conn = pymysql_conn()
    cursor = conn.cursor()
    sql = 'DELETE FROM '+table+' where TO_DAYS(NOW())-TO_DAYS(create_time)>7'
    # sql = 'truncate table '+table
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    
def main():
    for table in tables:
        truncate(table)

if __name__ == '__main__':
    main()

# DELETE FROM tb WHERE CreateTime BETWEEN '2017-01-01 00:00:00' AND '2017-02-01 00:00:00'


