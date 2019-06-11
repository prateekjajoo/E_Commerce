from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


gender_choices = [
    ('M', 'Male'),
    ('F', 'Female')
]

category_choices = [
    ('mobile', 'Mobile'),
    ('television', 'Television'),
    ('refrigerator', 'Refrigerator')
]


# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=30, choices=category_choices, default='None', null=True, blank=True)
    company_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=150, null=True, blank=True)
    specification = HTMLField(blank=True, default=u'')
    prize = models.CharField(max_length=15)
    image = models.ImageField(default='', blank=True, null=True)

    def __str__(self):
        return str(self.model_name)


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(default='', blank=True, null=True)


class Seller(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=10, choices=gender_choices, default='None', null=True, blank=True)
    mobile = models.CharField(max_length=15)


class BestOffer(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    best_prize = models.CharField(max_length=150)
