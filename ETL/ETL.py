from ODS.mysql2hive_spark import ods_run
from DWD.ods2dwd_spark import dwd_run
from DWD.hive2mysql_spark import dwd_mysql_run
from ALS.train import train_run

if __name__ == '__main__':
    ods_run()
    dwd_run()
    dwd_mysql_run()
    train_run()