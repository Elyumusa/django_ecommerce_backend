from django.db import models
from django.contrib.auth.models import User
from core.models import Product

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "{}/{}".format(self.userId.username,self.product.title)
# Create your models here.
