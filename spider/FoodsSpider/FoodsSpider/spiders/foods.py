import scrapy
from scrapy.http import Request
from time import sleep
from scrapy.utils.project import get_project_settings
import datetime,json
settings = get_project_settings()


class SteamSpider(scrapy.Spider):
    Types_url = [i[0]+'hot-%s/' for i in settings.get("TYPES")]
    Types_name = [i[1] for i in settings.get("TYPES")]
    name = "foods"
    type_index = 0
    allowed_domains = ["xiangha.com"]
    page=1
    start_urls = [Types_url[0]%(page)]
    
    custom_settings = {
        "ITEM_PIPELINES": {
            "FoodsSpider.pipelines.DefaultPipeline": 300,
        },
        "DEFAULT_REQUEST_HEADERS": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "webCode=ed8bc06acfeb0000; __51cke__=; Hm_lvt_b4e54a90a585580f47284f3fe21da41b=1711698638; _bl_uid=6nlyCu4Ic00dqv6dd9Lzuy6f33g3; SERVERID=f063cc9e8ade7891ff956cebb9aa6400|1711700430|1711700404; SERVERCORSID=f063cc9e8ade7891ff956cebb9aa6400|1711700430|1711700404; xhRecord=pv:7,deep:7,; __tins__21782439=%7B%22sid%22%3A%201711700443698%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201711702243698%7D; __51laig__21782439=7; __tins__21295193=%7B%22sid%22%3A%201711700443699%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201711702243699%7D; __51laig__21295193=7; Hm_lpvt_b4e54a90a585580f47284f3fe21da41b=1711700444",
            "Referer": "https://www.xiangha.com/caipu/z-sucai/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
            "sec-ch-ua": '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        },
    }
    def parse_detail(self, response, data):
        # 处理详情页面内容
        # 提取需要的数据
        
        detail_data = {}
        detail_data['raw_detail']=json.dumps([i.xpath('string()').get()  for i in response.xpath("//*[@class='rec_ing']//td")],ensure_ascii=False)
        detail_data['cookbook_make']=json.dumps([i.xpath('string()').get() for i in response.xpath("//*[@id='CookbookMake']//p")],ensure_ascii=False)
        data_res= {
            **data,
            **detail_data
        }
        self.logger.info(
                f"msg:爬取成功,name:{data['name']},url:{data['url']},data:{data_res}"
            )
        
        yield data_res
    def parse(self, response):
        try:
            self.logger.info(
                f"msg:开始爬取,name:{self.Types_name[self.type_index]}-page:{self.page},url:{response.url}"
            )
            
            for li in response.xpath('//div[@class="s_list tab_con"]/ul/li') :
                data={}
                data['name']=li.xpath('./a/@title').get()
                data['url']=li.xpath('./a/@href').get()
                data['raw']=li.xpath('string(./div[@class="ins"]/p[@class="info"][1])').get().replace("用料：",'')
                data['type']=self.Types_name[self.type_index]
                data['img']=li.xpath('./a/img/@src').get()
                data["crawler_date"]=datetime.datetime.now()
                self.logger.info(
                f"msg:开始爬取,name:{data['name']},url:{data['url']}"
                )
                yield scrapy.Request(url=data['url'], callback=self.parse_detail, cb_kwargs={'data': data})
            self.logger.info(
                f"msg:爬取成功,type:{self.Types_name[self.type_index]}-page:{self.page},url:{response.url}"
            )
            if response.xpath("//*[@class='nextpage']")!=[]:
                self.page+=1
                yield Request(self.Types_url[self.type_index]%(self.page), callback=self.parse, dont_filter=True)
            else:
                if self.type_index<len(self.Types_url)-1:
                    self.page=1
                    self.type_index+=1
                    yield Request(self.Types_url[self.type_index]%(self.page), callback=self.parse, dont_filter=True)

        except Exception as e:
            self.logger.error(
                f"msg:请求异常{e},type:{self.Types_name[self.type_index]}-page:{self.page},url:{response.url}"
            )
            sleep(60)
            yield Request(response.url%(self.page), callback=self.parse, dont_filter=True)
