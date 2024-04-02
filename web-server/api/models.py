from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from json import dumps,loads
def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = 'headerpic.'+ext
    return os.path.join(str(instance), filename)  # 系统路径分隔符差异，增强代码重用性

class Foods(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    raw=models.TextField( verbose_name='原料',default=0, null=True,blank=True)
    type = models.CharField(verbose_name='类型',max_length=255,blank=True, null=True)
    type_code=models.IntegerField(verbose_name='类型编码',default=0,null=True,blank=True)
    img=models.TextField(blank=True, null=True)
    raw_detail=models.TextField(verbose_name='原料用量', null=True,blank=True)
    cookbook_make=models.TextField(verbose_name='制作方法' ,null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True,db_column='crawler_date')  # 添加创建时间字段

    def to_dict(self,type):
        # 将模型实例转换为字典
        job_dict = {
            'id':self.id,
            'type':type,
            'name':self.name,
            'raw':self.raw,
            'type2':self.type,
            'type_code':self.type_code,
            'raw_detail':self.raw_detail,
            'cookbook_make':self.cookbook_make,
            'url':self.url,
            'img':self.img,
            'create_time':self.create_time 
        }
        # 将字典转换为JSON字符串并返回
        return job_dict
    def __str__(self):
        return f'{self.name}'
    class Meta:
        managed = False
        verbose_name = '食谱列表'
        db_table = 'foods'
        verbose_name_plural = verbose_name
class UserResume(models.Model):
    class Sex(models.TextChoices):
        男 = '1'
        女 = '0'
    id=models.BigAutoField(primary_key=True)
    user=models.OneToOneField('api.user', on_delete=models.CASCADE,null=True,blank=True)
    type1=models.IntegerField(verbose_name='期望菜品类型id',default=0,null=True,blank=True)
    type1Translation=models.CharField(max_length=20, verbose_name='期望菜品类型', null=True,blank=True)
    type2=models.IntegerField(verbose_name='期望菜品类型2id',default=0,null=True,blank=True)
    type2Translation=models.CharField(max_length=20, verbose_name='期望菜品类型2', null=True,blank=True)
    type3=models.IntegerField(verbose_name='期望菜品类型3id',default=0,null=True,blank=True)
    type3Translation=models.CharField(max_length=20, verbose_name='期望菜品类型3', null=True,blank=True)

    
    
    created_time = models.DateTimeField(auto_now_add=True)  # 添加创建时间字段
    last_update = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')
    def to_dict(self):
        resume_data = {
            'id': self.id,
            'user_id': self.user.id,
            'name': self.user.name,
            'email':self.user.email,
            "phone":self.user.phone,
            'photo':'/media/'+str(self.user.photo),
            'birth': self.user.birth.strftime('%Y-%m-%d') if self.user.birth else '',
            'genderCode': str(self.user.genderCode).replace("None",""),
            'genderTranslation': self.user.genderTranslation,
            'type1': str(self.type1).replace("None",""),
            'type2': str(self.type2).replace("None",""),
            'type3': str(self.type3).replace("None",""),
            'type1Translation': self.type1Translation,
            'type2Translation': self.type2Translation,
            'type3Translation': self.type3Translation,
            'created_time': self.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'last_update': self.last_update.strftime('%Y-%m-%d %H:%M:%S'),
        }

        return resume_data
    class Meta:
        verbose_name = '用户画像信息'
        db_table = 'resume'
        verbose_name_plural = verbose_name
    
    
class user(AbstractUser):

    name=models.CharField(max_length=10, verbose_name='姓名',null=True)
    birth=models.DateField(verbose_name='生日',null=True)
    genderCode= models.IntegerField(  default='1', verbose_name='性别id 男 1 女 0',null=True)
    genderTranslation= models.CharField(max_length=2, default='男', verbose_name='性别',null=True)
    phone = models.CharField(max_length=11, verbose_name='手机号', null=False)
    photo = models.ImageField('头像', upload_to=user_directory_path, blank=True, null=True,default='default/user.jpg')
    resume_id=models.IntegerField(  blank=True,null=True)
    init = models.BooleanField('初始化', blank=True, null=True,default=False)
    last_update = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')    
    def __str__(self):
        return f'{self.username}'
    class Meta:
        verbose_name = '用户信息'
        db_table = 'user'
        verbose_name_plural = verbose_name


class Logs(models.Model):
    lid=models.BigAutoField(primary_key=True)
    user=models.ForeignKey(user, verbose_name="用户", on_delete=models.DO_NOTHING,null=True)
    active=models.TextField(verbose_name='行为')
    content=models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now=False,auto_now_add=True, verbose_name='创建时间')
    class Meta:
        verbose_name = '操作日志'
        db_table = 'logs'
        verbose_name_plural = verbose_name
        
class Recommendforallusers(models.Model):
    user_id = models.IntegerField(primary_key=True)
    recommendations = models.TextField(blank=True, null=True)
    @property
    def recommend_foods_list(self):
        li=[i for i in eval(self.recommendations)]
        return [list(j)[1] for j in li]
    class Meta:
        verbose_name = '用户推荐'
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'recommendforallusers'
        
class Starfoods(models.Model):
    sid=models.BigAutoField(primary_key=True)
    user=models.ForeignKey('api.user', verbose_name="用户", on_delete=models.CASCADE)
    foods=models.ForeignKey('api.foods', verbose_name="景点", on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=False,auto_now_add=True, verbose_name='创建时间')
    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name
        db_table = 'star'
class Commentfoods(models.Model):
    cid=models.BigAutoField(primary_key=True)
    user=models.ForeignKey('api.user', verbose_name="用户", on_delete=models.CASCADE)
    foods=models.ForeignKey('api.foods', verbose_name="景点", on_delete=models.CASCADE)
    content=models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now=False,auto_now_add=True, verbose_name='创建时间')
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        db_table = 'comment'   
class Likefoods(models.Model):
    cid=models.BigAutoField(primary_key=True)
    user=models.ForeignKey('api.user', verbose_name="用户", on_delete=models.CASCADE)
    foods=models.ForeignKey('api.foods', verbose_name="景点", on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=False,auto_now_add=True, verbose_name='创建时间')
    last_update = models.DateTimeField(auto_now=True,auto_now_add=False, verbose_name='最后修改时间')

    class Meta:
        verbose_name = '喜欢'
        db_table = 'like'
        verbose_name_plural = verbose_name

@receiver(post_save, sender=user)
def createResume(sender, instance, **kwargs):
    resume=UserResume.objects.filter(user=instance)
    if not resume.exists():
        r=UserResume.objects.create(user=instance)
