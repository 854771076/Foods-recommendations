from rest_framework import viewsets
from .serializers import *
from api.models import *
from rest_framework.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.decorators import action
import csv
from django.db.models import  *
from django.db.models.functions import *
from rest_framework import permissions
from rest_framework.response import Response
import random

from rest_framework import generics
from django.db.models import Q

class SimilarFoodsList(generics.ListAPIView):
	serializer_class = FoodsSerializer

	def get_queryset(self):
		id = self.kwargs.get('id')
		foods = Foods.objects.get(id=id)

		query = (
			Q(type=foods.type) 
		)

		similar_Foods = Foods.objects.filter(query).exclude(id=id)
		return similar_Foods


def get_random_objects(queryset, num_objects):
	random_objects = []
	total_objects = queryset.count()
	if num_objects >= total_objects:
		return list(queryset)
	while len(random_objects) < num_objects:
		random_index = random.randint(0, total_objects - 1)
		random_object = queryset[random_index]
		if random_object not in random_objects:
			random_objects.append(random_object)
	return random_objects
class CustomPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		# 在这里编写权限逻辑，返回 True 表示有权限，返回 False 表示没有权限
		if request.method=='GET' or (  request.method=='POST' ):
			return True
		else:
			
			return False
	def has_object_permission(self, request, view, obj):
		# 在这里编写对象级别的权限逻辑，返回 True 表示有权限，返回 False 表示没有权限
		return True


class FoodsFilter(filters.FilterSet):
	id = filters.CharFilter(lookup_expr='exact')
	type = filters.CharFilter(lookup_expr='icontains')


	class Meta:
		model = Foods
		fields = '__all__'
class FoodsViewSet(viewsets.ModelViewSet):
	authentication_classes = [JWTAuthentication]
	# 搜索
	filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
	search_fields = ('name',)
	filterset_class =FoodsFilter
	permission_classes = [CustomPermission]
	ordering_fields = ('crawler_date')
	queryset = Foods.objects
	serializer_class =FoodsSerializer
	lookup_field ='id'
	
	@action(detail=False, methods=['POST'])
	def like(self,request):
		data={
			'code':'200',
			'data':None,
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=CollectSerializer(data=request.data)
				if serializer.is_valid():
					id=serializer.validated_data.get('id')
					foods=Foods.objects.filter(id=id).first()
					like=Likefoods.objects
					if like.filter(user=request.user,foods=foods).exists():
						data['code']='-1'
						data['msg']='已点赞'
						return Response(data)
					like.create(user=request.user,foods=foods)
					data['data']=foods.to_dict('点赞')
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['POST'])
	def isliked(self,request):
		data={
			'code':'200',
			'data':None,
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=CollectSerializer(data=request.data)
				if serializer.is_valid():
					id=serializer.validated_data.get('id')
					foods=Foods.objects.filter(id=id).first()
					like=Likefoods.objects
					if like.filter(user=request.user,foods=foods).exists():
						data['data']=True
						data['msg']='已点赞'
						return Response(data)
					data['data']=False
					data['msg']='未点赞'
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['POST'])
	def removelike(self,request):
		data={
			'code':'200',
			'data':None,
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=CollectSerializer(data=request.data)
				if serializer.is_valid():
					id=serializer.validated_data.get('id')
					foods=Foods.objects.filter(id=id).first()
					
					like=Likefoods.objects
					if not like.filter(user=request.user,foods=foods).exists():
						data['code']='-1'
						data['msg']='未点赞'
						return Response(data)
					like.filter(user=request.user,foods=foods).delete()
					data['data']=foods.to_dict('取消点赞')
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['POST'])
	def collect(self,request):
		data={
			'code':'200',
			'data':None,
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=CollectSerializer(data=request.data)
				if serializer.is_valid():
					id=serializer.validated_data.get('id')
					foods=Foods.objects.filter(id=id).first()
					star=Starfoods.objects
					if star.filter(user=request.user,foods=foods).exists():
						data['code']='-1'
						data['msg']='已收藏'
						return Response(data)
					star.create(user=request.user,foods=foods)
					data['data']=foods.to_dict('收藏')
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['GET'])
	def collectFoods(self,request):
		data={
			'code':'200',
			'data':[],
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=RecommendSerializer(data=request.GET)
				if serializer.is_valid():
					page=serializer.validated_data.get('page')
					pagesize=serializer.validated_data.get('pagesize')
					res=Starfoods.objects.filter(user=request.user)
					foods_list=[i.foods.to_dict(None) for i in res[(page-1)*pagesize:page*pagesize]]
					data['count']=res.count()
					data['data']=foods_list
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['POST'])
	def comment(self,request):
		data={
			'code':'200',
			'data':None,
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=CollectSerializer(data=request.data)
				content=request.data.get('content')
				if serializer.is_valid() and content:
					id=serializer.validated_data.get('id')
					foods=Foods.objects.filter(id=id).first()
					Comment=Commentfoods.objects

					Comment.create(user=request.user,foods=foods,content=content)
					data['data']='ok'
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['GET'])
	def commentFoods(self,request):
		data={
			'code':'200',
			'data':[],
			'msg':'ok',
		}
		try:
			serializer=RecommendSerializer(data=request.GET)
			oid=int(request.GET.get('id'))
			if serializer.is_valid() and oid:
				page=serializer.validated_data.get('page')
				pagesize=serializer.validated_data.get('pagesize')
				t=Foods.objects.get(id=oid)
				foods_list=[{'id':i.cid,'username':i.user.username,'content':i.content,'create_time':i.create_time} for i in Commentfoods.objects.filter(foods=t).order_by('-create_time')[(page-1)*pagesize:page*pagesize]]
				data['count']=Commentfoods.objects.filter(foods=t).count()
				data['data']=foods_list
			else:
				# 参数有误
				data['code']='-1'
				data['msg']=serializer.errors	
		except Exception as e:
			data['code']='-1'
			data['data']=str(e)
			data['msg']='系统错误'

		return Response(data)
	@action(detail=False, methods=['GET'])
	def likeFoods(self,request):
		data={
			'code':'200',
			'data':[],
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=RecommendSerializer(data=request.GET)
				if serializer.is_valid():
					page=serializer.validated_data.get('page')
					pagesize=serializer.validated_data.get('pagesize')
					res=Likefoods.objects.filter(user=request.user)
					foods_list=[i.foods.to_dict(None) for i in res[(page-1)*pagesize:page*pagesize]]
					data['count']=res.count()
					data['data']=foods_list
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['POST'])
	def iscollected(self,request):
		data={
			'code':'200',
			'data':None,
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=CollectSerializer(data=request.data)
				if serializer.is_valid():
					id=serializer.validated_data.get('id')
					foods=Foods.objects.filter(id=id).first()
					star=Starfoods.objects
					if star.filter(user=request.user,foods=foods).exists():
						data['data']=True
						data['msg']='已收藏'
						return Response(data)
					data['data']=False
					data['msg']='未收藏'
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['POST'])
	def removecollect(self,request):
		data={
			'code':'200',
			'data':None,
			'msg':'ok',
		}
		if request.user.is_authenticated:
			try:
				serializer=CollectSerializer(data=request.data)
				if serializer.is_valid():
					id=serializer.validated_data.get('id')
					foods=Foods.objects.filter(id=id).first()
					
					star=Starfoods.objects
					if not star.filter(user=request.user,foods=foods).exists():
						data['code']='-1'
						data['msg']='未收藏'
						return Response(data)
					star.filter(user=request.user,foods=foods).delete()
					data['data']=foods.to_dict('取消收藏')
				else:
					# 参数有误
					data['code']='-1'
					data['msg']=serializer.errors	
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			data['code']=-1
			data['msg']='请登录'
		return Response(data)
	@action(detail=False, methods=['GET'])
	def recommend(self,request):
		data={
			'code':'200',
			'data':None,
			'msg':'ok',
			'count':200
		}
		serializer=RecommendSerializer(data=request.GET)
		if serializer.is_valid():
			try:
				page=serializer.validated_data.get('page')
				pagesize=serializer.validated_data.get('pagesize')
				maxpage=10
				#最新随机列表limit
				newlimit=1000
				foods=Foods.objects.order_by('-id')[:newlimit]
				if request.user.is_authenticated :
					user_id=request.user.id
					if page==1:
						#首页实时推荐，根据收藏推荐
						star_foods_list=[i.foods for i in Starfoods.objects.filter(user_id=user_id).order_by('create_time')] 
						star_user_list=[i.user for i in Starfoods.objects.filter(foods__in=star_foods_list[:100]).exclude(user_id=user_id).distinct()]
						#点击
						click_foods_list=[i.foods for i in Likefoods.objects.filter(user_id=user_id).order_by('create_time')] 
						click_user_list=[i.user for i in Starfoods.objects.filter(foods__in=click_foods_list[:100]).exclude(user_id=user_id).distinct()]
						similar_foods_list=Starfoods.objects.values('foods').filter(user__in=star_user_list[:100]).union(Likefoods.objects.values('foods').filter(user__in=click_user_list[:100]))
						foods_list=[Foods.objects.get(id=i.get('foods')).to_dict('实时') for i in get_random_objects(similar_foods_list,pagesize//2)]
						length=len(foods_list)
						if length<pagesize:
							
							# 热门数据填充
							foods_id_list = [i.id for i in get_random_objects(foods,pagesize-length)]
							foods_list+=[i.to_dict('热门') for i in Foods.objects.filter(id__in=foods_id_list[:pagesize-length])]
						#填充完还小于pagesize条，使用foods数据随机填充
						length=len(foods_list)
						if length<pagesize:
							foods_list+=[i.to_dict('最新随机') for i in get_random_objects(foods,pagesize-length)]
					else:
						#如果有离线推荐数据
						Rrecommend=Recommendforallusers.objects.filter(user_id=user_id)
						if Rrecommend.exists():
							foods_id_list=Rrecommend.first().recommend_foods_list[(page-2)*pagesize:(page-1)*pagesize]
							foods_list=[i.to_dict('匹配') for i in Foods.objects.filter(id__in=foods_id_list)]
						else:
							# 热门数据填充
							# 获取热门的 foods_list
							foods_id_list = [i.id for i in  get_random_objects(foods,pagesize-length)]
							foods_list=[i.to_dict('热门') for i in Foods.objects.filter(id__in=foods_id_list)]
							if foods_list==[] or len(foods_list)<pagesize:
								foods_list+=[i.to_dict('最新随机') for i in get_random_objects(foods,pagesize-len(foods_list))]

				else:
					if page==1:
						# 热门数据填充
						foods_id_list = [i.id for i in  get_random_objects(foods,pagesize-length)]
						foods_list=[i.to_dict('热门') for i in Foods.objects.filter(id__in=foods_id_list)]
						#最新随机数据填充
						if foods_list==[] or len(foods_list)<pagesize:
								foods_list+=[i.to_dict('最新随机') for i in get_random_objects(foods,pagesize-len(foods_list))]
					else:
						foods_list=[i.to_dict('最新随机') for i in get_random_objects(foods,pagesize)]
				data['data']=foods_list
				data['page']=page
			except Exception as e:
				data['code']='-1'
				data['data']=str(e)
				data['msg']='系统错误'
		else:
			# 参数有误
			data['code']='-1'
			data['msg']=serializer.errors
		return Response(data)
	@action(detail=False, methods=['GET'])	
	def bigdata_info(self, request):
		

		queryset = self.filter_queryset(self.get_queryset())
		data={}
		data['count']=user.objects.aggregate(sum=Count('id')).values() 
		data['total']=queryset.aggregate(sum=Count('id')).values() 
		return Response({'msg':'OK','code':'200','data':data})
	@action(detail=False, methods=['GET'])	
	def like_info(self, request):
		total=Likefoods.objects.aggregate(sum=Count('cid')).values() 
		data=Likefoods.objects.values('foods__type').annotate(name=F('foods__type'),sum=Count('cid')).order_by('-sum')[:5]
		return Response({'msg':'OK','code':'200','data':data,'total':total})
	
	@action(detail=False, methods=['GET'])	
	def foods_type_info(self, request):
		queryset = self.filter_queryset(self.get_queryset())
		data=queryset.values('type').annotate(name=F('type'),value=Count('id')).order_by('-value')[:10]
		return Response({'msg':'OK','code':'200','data':data})
	@action(detail=False, methods=['GET'])	
	def star_info(self, request):
		total=Starfoods.objects.aggregate(sum=Count('sid')).values() 
		data=Starfoods.objects.values('foods__type').annotate(name=F('foods__type'),value=Count('sid')).order_by('-value')[:10]
		return Response({'msg':'OK','code':'200','data':data,'total':total})
	
	@action(detail=False, methods=['GET'])	
	def foods_routype_info(self, request):


		queryset = self.filter_queryset(self.get_queryset())
		data=queryset.filter(type__icontains='肉').values('type').annotate(name=F('type'),value=Count('id')).order_by('-value')[:10]
		return Response({'msg':'OK','code':'200','data':data})