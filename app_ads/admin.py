from django.contrib import admin
from models import AdsCategory, Advertiser

class AdsCategoryAdmin(admin.ModelAdmin):
    pass


class AdsAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdsCategory)
admin.site.register(Advertiser)