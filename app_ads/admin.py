from django.contrib import admin
from app_ads.models import AdsCategory, Advertiser, Notification

class AdsCategoryAdmin(admin.ModelAdmin):
    list_filter = ('id', 'category_name')
    list_display = ('id', 'category_name')
    search_fields = ('category_name', 'category_info')


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id','user_Id', 'ad_title','created_at', 'is_active')
    list_filter = ('user_Id', 'ad_title', 'ad_category','ad_condition', 'is_active')
    search_fields = (
        'id', 'user_Id', 'ad_title', 'ad_description',
        'ad_condition', 'ad_category', 'created_at',
        'updated_at', 'is_active'
                     )


admin.site.register(AdsCategory, AdsCategoryAdmin)
admin.site.register(Advertiser, AdsAdmin)
admin.site.register(Notification)