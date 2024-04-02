from django.contrib import admin
from api.models import *
from django.contrib.admin import DateFieldListFilter
# Register your models here.
admin.site.site_header='后台管理'
admin.site.site_title='后台管理'
@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','last_login') # list
    search_fields = ('username',)
    ordering=['-date_joined']
    list_filter=[('date_joined',DateFieldListFilter)]

@admin.register(Recommendforallusers)
class RecommendforallusersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'recommendations') # list
    search_fields = ('user_id',)
    list_filter=['user_id']



@admin.register(UserResume)
class UserResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','type1Translation','type2Translation','type3Translation') # list
    search_fields = ('user__username',)
    ordering=['-created_time','-last_update']
    list_filter=['user']

@admin.register(Foods)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','type') # list
    search_fields = ('name',)
    list_filter=['type']

@admin.register(Starfoods)
class StarFoodsAdmin(admin.ModelAdmin):
    list_display = ('user', 'foods','create_time') # list
    search_fields = ('user_id',)
    ordering=['-create_time']
    list_filter=['user_id', 'foods_id']
    list_display_links =['user', 'foods']
@admin.register(Likefoods)
class ClickFoodsAdmin(admin.ModelAdmin):
    list_display = ('user', 'foods','create_time','last_update') # list
    search_fields = ('user_id',)
    ordering=['-create_time','-last_update']
    list_filter=['user_id', 'foods_id']
    list_display_links =['user', 'foods']
@admin.register(Commentfoods)
class ClickFoodsAdmin(admin.ModelAdmin):
    list_display = ('user', 'foods','create_time','content') # list
    search_fields = ('user_id',)
    ordering=['-create_time']
    list_filter=['user_id', 'foods_id']
    list_display_links =['user', 'foods']