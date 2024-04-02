import pymysql
from sqlalchemy import create_engine
import pandas as pd

class MysqlDB():
    def __init__(self,user='root',password='123456',host='127.0.0.1',port=3306,charset='utf8',db='spider',**params):
        
        self.conn=create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset={charset}',echo=False)
    def save_pd(self,val,table:str,columns=None,method:str='replace'):
        '''
        method append,replace
        '''
        
        if columns!=None:
            df=pd.DataFrame(val,columns=columns)
        else:
            df=pd.DataFrame(val)
        df.to_sql(table,self.conn,if_exists=method,index=False)
        return df
    def read_pd(self,table:str):
        df=pd.read_sql_table(con=self.conn,table_name=table)
        return df 