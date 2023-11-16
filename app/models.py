from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
('FC', 'Fashion'),
('FOC', 'Food Products Coupons'),
('SC', 'Shoes Coupons'),
('CC', 'Clothing Coupons'),
('SPC', 'Shopping Coupons'),
('EC', 'Electronics Coupons'),
('TCC', 'Travel Coupons Coupons'),
('ZSC', 'Zomato/swiggy Coupons'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description= models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category= models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to= 'product')
    def __str__(self):
        return self.title
