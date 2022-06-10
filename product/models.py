from django.db import models

# Create your models here.

# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.CharField()
#     # characteristic = 
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     amount = models.BooleanField()
#     category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

#     def __str__(self):
#         return self.title 

# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)

#     def __str__(self):
#         return self.name