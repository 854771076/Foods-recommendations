from common.SparkMySQLHiveETL import *
def ods_run():
    TASK=[
        
        {"name": "爬虫数据", "source_db": "spider", "source_tb": "foods", "db_num": 0, "t_num": 0,
         'sink_db': 'ods_foods', 'sink_tb': 'ods_foods_db_spider_t_foods', "update_column": "crawler_date",'partition_column':'partition_date','is_del':True,},
        {"name": "用户简历信息", "source_db": "foods", "source_tb": "resume", "db_num": 0, "t_num": 0,
         'sink_db': 'ods_foods', 'sink_tb': 'ods_foods_db_foods_t_resume', "update_column": "last_update",'partition_column':'partition_date','is_del':True,}
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
    a=SparkMySQLHiveETL(DB_LOG_PARAMS=MYSQL_CONNECT,MYSQL_PARAMS=MYSQL_PARAMS,appName='ods',Task=TASK,TYPE='all',maxProcess=1,maxWorkers=1)
    a.yesterday_time=date.today()
    a.partition_date=a.yesterday_time.strftime("%Y%m%d")
    a.today_time=a.today_time+timedelta(days=1)
    a.run()