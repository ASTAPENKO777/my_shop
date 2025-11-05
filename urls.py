from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    path('', views.shop_page, name='shop'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('index', views.index, name='index'),
    path('customers', views.customer, name='customers'),
    path('orders', views.orders, name='orders'),
    path('categorys', views.category, name='categorys'),
]

urlpatterns += staticfiles_urlpatterns()
