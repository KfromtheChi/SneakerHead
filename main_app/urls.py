from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('icons/', views.index, name='index'),
    path('user_sneakers/', views.sneaker_index, name='sneaker_index'),
    path('icons/<int:icon_id>/', views.icons_detail, name='detail'),
    path('user_sneakers/<int:user_sneaker_id>/', views.sneaker_detail, name='sneaker_detail'),
    path('user_sneakers/create/', views.UserCreate.as_view(), name='user_create'),
    path('user_sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneaker_update'),
    path('user_sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneaker_delete'),
]