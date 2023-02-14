from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_discrip = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://covesurfandturf.com/wp-content/uploads/2021/09/food-placeholder-1.jpg')
    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})

class Basic(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    def __str__(self):
        return self.item_name