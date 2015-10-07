from django.db import models

# Create your models here.
class Products(models.Model):
	name = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	cost = models.IntegerField()