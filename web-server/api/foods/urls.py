from django.urls import path,include
from api.foods.foodsviews import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'foods',FoodsViewSet)
urlpatterns = [
    path('similar/<str:id>/', SimilarFoodsList.as_view()),
]
urlpatterns += router.urls