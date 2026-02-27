from django.db import models
from django.utils.text import slugify


# Create your models here.
class SellerProfile(models.Model):
    shop_name=models.CharField(max_length=100)
    password=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15,unique=True)
    address=models.TextField()
    pincode=models.CharField(max_length=6)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    gst_number=models.CharField(max_length=100,blank=True,null=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, blank=True)
    image=models.ImageField(upload_to="category_icons/", null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return self.name
      
class Notification(models.Model):
    seller=models.ForeignKey(SellerProfile,on_delete=models.CASCADE)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Discount(models.Model):
    code=models.CharField(max_length=50, unique=True)
    percentage=models.DecimalField( max_digits=5,decimal_places=2)
    valid_from=models.DateTimeField()
    valid_to = models.DateTimeField()
    is_active = models.BooleanField(default=True)