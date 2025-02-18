from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_view),
    # path('detail/<int:pk>',views.car_detail_view, name='detail'),
    # path('category/<str:category_title>',views.category_view, name='category'),
    path('news_create/', views.news_create_view),
    path('car_create/', views.car_create_view),
]