from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    # path('home/',views.home,name='index'),
    path('newcustomer',views.newcustomer,name='newcustomer'),
    path('allcustomer',views.allcustomer,name='allcustomer'),
    path('transfer/<str:pk>/',views.customer_detail,name='transfer')
]
