from django.urls import path
from Order import views

app_name = 'Order'

urlpatterns = [
    path('create_order/', views.Order_create, name='Order_create'),
    path('orders/', views.Order_list, name='Order_list')
]