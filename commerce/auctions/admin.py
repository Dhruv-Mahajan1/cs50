from django.contrib import admin
from .models import User,Listing,Bids,Comments,Wishlist

# class UserAdmin(admin.ModelAdmin):
#     list_display = ("id", )

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(Wishlist)
