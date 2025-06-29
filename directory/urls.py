from django.urls import path
from . import views

app_name = 'directory'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('search/', views.search, name='search'),
]