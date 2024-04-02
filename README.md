[toc]

# 食谱推荐系统



### 一、系统账号

* 前台

http://127.0.0.1:8000

`root/12345678`

* 后台

http://127.0.0.1:8000/admin

`root/12345678`

### 二、项目架构

#### 2.1 总架构图

![系统架构](doc\系统架构.png)

#### 2.2 数仓架构

![系统架构](doc\数仓架构.png)

#### 2.3 功能设计

![系统架构](doc\系统功能设计.png)

#### 2.4 ER图

![系统架构](doc\ER图.png)

### 三、项目部署

### 3.1 环境初始化

* 下载Anaconda

* 下载MySQL和Redis数据库

* 创建虚拟环境

  * 爬虫环境

  ```cmd
  conda create -n Spider python=3.8
  pip install -r .\spider\FoodsSpider\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
  ```

  * Web环境

  ```cmd
  conda create -n web python=3.8
  pip install -r .\web-server\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
  ```

### 3.2 项目启动

#### 3.2.1 爬虫程序

##### 正常启动

* 切换至Spider环境

  ```cmd
  conda activate jobfreeSpider
  ```

* 修改Foods-recommendations\spider\FoodsSpider\FoodsSpider\settings.py的mysql连接配置

* ![image-20240401174853904](img\1.png)

* 执行Foods-recommendations\spider\FoodsSpider\FoodsSpider\spider\run.py启动scrapy

* ![image-20240401174853904](img\2.png)

  


#### 3.2.2 Web程序

##### 配置settings.py

```python
# web-server\DRF\settings.py
# SMTP邮箱设置,怎么申请请自行网上学习
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''  # 邮箱SMTP服务器地址
EMAIL_HOST_USER = ''  # 邮箱用户名
EMAIL_HOST_PASSWORD = ''  # 邮箱密码
# EMAIL_USE_TLS = True  # 使用TLS加密
DEFAULT_FROM_EMAIL = ''  # 默认发件人邮箱
#redis
REDIS_HOST='127.0.0.1'
REDIS_PORT=6379
REDIS_PSW=''
REDIS_DB=1
#MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foods',  
        'USER': 'root',  
        'PASSWORD': 'root',  
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    },

}
```

##### 迁移数据库

```cmd
conda activate jobfree
cd web-server
python manage.py migrate
```

##### windows一键启动

> 双击web-start.bat

##### 正常启动

```cmd
cd web-server
conda activate web
python manage.py runserver
```

#### 3.2.3 ETL模块

##### 环境搭建

> 有集群则跳过

[Windows下使用hadoop+hive+sparkSQL-CSDN博客](https://blog.csdn.net/qq_41631913/article/details/134804263)

##### 安装python库

```cmd
pip install findspark
```

##### 执行ETL脚本

> ETL\xxx目录下的py文件

##### 模型训练

> ETL\ALS\train_run.py
