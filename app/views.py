from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, CATEGORY_CHOICES


def home(request):
    trending = Product.objects.all()[:8]
    categories = CATEGORY_CHOICES
    return render(request, 'app/home.html', {
        'trending': trending,
        'categories': categories,
    })


def browse(request):
    products = Product.objects.all()
    categories = CATEGORY_CHOICES
    return render(request, 'app/browse.html', {
        'products': products,
        'categories': categories,
    })


class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        categories = CATEGORY_CHOICES
        # Get current category name
        current_category = dict(CATEGORY_CHOICES).get(val, 'All')
        return render(request, 'app/browse.html', {
            'products': products,
            'categories': categories,
            'current_category': current_category,
            'current_val': val,
        })


def coupon_detail(request, pk):
    coupon = get_object_or_404(Product, pk=pk)
    related = Product.objects.filter(category=coupon.category).exclude(pk=pk)[:4]
    return render(request, 'app/coupon_detail.html', {
        'coupon': coupon,
        'related': related,
    })


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')
