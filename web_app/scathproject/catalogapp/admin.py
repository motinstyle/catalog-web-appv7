from django.contrib import admin
from .models import products, users, UserCards

# Register your models here.
admin.site.register(products)
admin.site.register(users)
admin.site.register(UserCards)
