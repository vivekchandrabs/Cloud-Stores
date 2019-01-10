from django.contrib import admin
from dbapp.models import *
# Register your models here.

admin.site.register(UserDetail)
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(OrderShop)
admin.site.register(Order_Item)

