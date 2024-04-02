from common.SparkMySQLHiveETL import *

def dwd_mysql_run():
    TASK = [
        {"name": "爬虫数据", "sink_db": "foods", "sink_tb": "foods", "db_num": 0, "t_num": 0,
         'source_db': 'dwd_foods', 'source_tb': 'dwd_foods_db_spider_t_foods', "update_column": "cdc_sync_date",'is_del':True,'partition_column':'partition_date'},

    ]
    MYSQL_CONNECT = {
        'host': '10.8.16.253',
        'port': 3306,
        'user': 'root',
        'password': 'fiang123',
        'charset': 'utf8',
        'db': 'logs'
    }
    MYSQL_PARAMS = {
        'host': '10.8.16.253',
        'port': 3306,
        'user': 'root',
        'password': 'fiang123',
    }
    a = SparkMySQLHiveETL(DB_LOG_PARAMS=MYSQL_CONNECT, MYSQL_PARAMS=MYSQL_PARAMS, appName='dwd_2_mysql', Task=TASK,
                          TYPE='update',outType=2)
    a.yesterday_time = date.today()
    a.partition_date = a.yesterday_time.strftime("%Y%m%d")
    a.today_time = a.today_time + timedelta(days=1)
    a.run()