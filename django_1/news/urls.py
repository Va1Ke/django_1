from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDatailViev.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateViev.as_view(), name='news-detail'),
    path('<int:pk>/delete', views.NewsDeleteViev.as_view(), name='news-detail')
]
