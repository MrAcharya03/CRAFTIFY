from django.contrib import admin

# Register your models here.
from .models import Product, Customer,Cart,Payment,OrderPlaced,Wishlist

admin.site.register(Product),


admin.site.register(Customer)



admin.site.register(Cart)

admin.site.register(Payment)




admin.site.register(OrderPlaced)
admin.site.register(Wishlist)
