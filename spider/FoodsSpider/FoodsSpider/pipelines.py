# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from .utils import *
import datetime
from scrapy.utils.project import get_project_settings
settings = get_project_settings()




class DefaultPipeline:
    items=[]
    def open_spider(self, spider):
        # 建立连接
        self.conn = MysqlDB(**settings.get('MYSQL_CONNECT'))

    def process_item(self, item, spider):
        try:
            
            self.conn.save_pd([item],'foods',method='append')

        except Exception as e:
            spider.logger.error(item)
            spider.logger.error(e,item)
        
    def close_spider(self, spider):
        pass
