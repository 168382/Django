
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import  Customer,Order


# View to list all orders
def order_list(request):
    orders = Order.objects.all()
    data = {"orders": list(orders.values("id", "customer_id", "order_date", "total_amount"))}
    return JsonResponse(data)

# View to get details of a single order
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    data = {
        "id": order.id,
        "customer": order.customer.name,
        "order_date": order.order_date,
        "total_amount": order.total_amount,
    }
    return JsonResponse(data)
