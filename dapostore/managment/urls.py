from django.urls import path
from . import views
app_name = "managment"
urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('login/', views.admin_login, name="admin_login"),
    path('register/', views.admin_register, name='admin_register'),
    path('logout', views.admin_logout, name="admin_logout"),
    path('admin-products', views.admin_products, name="admin_products"),
]
