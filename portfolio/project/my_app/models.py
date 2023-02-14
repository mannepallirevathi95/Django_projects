from django.db import models

# Create your models here.

# About model
class About(models.Model):
    theme = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = "About myself"
        verbose_name_plural = "About myself"

    def __str__(self):
        return "About myself"

# service model
class Services(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Service name")
    description = models.TextField(verbose_name = "About service")

    def __str__(self):
        return self.name

# recent work model
class RecentWork(models.Model):
    title = models.CharField(max_lenghth = 100, verbose_name = "Work title")
    image = models.ImageField(upload_to = "works")

    def __str__(self):
        return self.title

# client model
class Client(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Client name")
    description = models.TextField(verbose_name = "Clint say")
    image = models.ImageField(upload_to = "clients", default = "default.png")

    def __str__(self):
        return self.name