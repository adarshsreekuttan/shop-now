from django.db import models
from seller.models import SubCategory
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=True,blank=True)

    price = models.IntegerField()
    discount_price = models.IntegerField()

    description = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products_image/',null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
