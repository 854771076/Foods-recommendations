from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework_simplejwt.views import TokenRefreshView
from app.views import *
urlpatterns = [
    path('', VueAppView.as_view(), name='vue_app'),
    path('login', VueAppView.as_view()),
    path('recommend', VueAppView.as_view()),
    path('Foods', VueAppView.as_view()),
    path('login', VueAppView.as_view()),
    path('star', VueAppView.as_view()),
    path('history', VueAppView.as_view()),
    path('guihua', VueAppView.as_view()),
    path('mine', VueAppView.as_view()),
    path('resume', VueAppView.as_view()),
    path('foods', VueAppView.as_view()),
    path('bigview', VueAppView.as_view()),
    re_path('foods/detail/*', VueAppView.as_view()),

    
    

]
