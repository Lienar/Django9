from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Buyer)
#admin.site.register(Game)

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "password", "age",)
    search_fields = ("name", "balance", "password", "age",)
    list_filter = ("balance",)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "cost", "size", "description", "age_limited")
    search_fields = ("title",)
    list_filter = ("cost",)

