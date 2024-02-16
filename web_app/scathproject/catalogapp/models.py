from django.db import models
from django.utils import timezone

# Create your models here.
class products(models.Model):
    path = models.TextField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.description
    

class users(models.Model):
    user_name = models.CharField(max_length=255)
    telegram_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    balance = models.FloatField()
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user_name


class UserCards(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    acquired_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'UserCards'
        verbose_name = 'User Card'
        verbose_name_plural = 'User cards'

    def __str__(self):
        return f"{self.user.user_name} - {self.product.category}"