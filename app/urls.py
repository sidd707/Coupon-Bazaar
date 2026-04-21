from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('coupon/<int:pk>/', views.coupon_detail, name='coupon_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
