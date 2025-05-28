from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

CONDITION_CHOICES = [
    ("new", "New"),
    ("used", "Used"),
    ("old", "Old"),
]

class AdsCategory(models.Model):
    category_name = models.CharField(max_length=250)
    category_info = models.TextField(max_length=500)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'ads_category'
        verbose_name = 'Ads Category'
        verbose_name_plural = 'Ads Categories'


class Advertiser(models.Model):
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_title = models.CharField(max_length=250, null=True, blank=True)
    ad_description = models.TextField(max_length=500, null=True, blank=True)
    ad_image = models.ImageField(upload_to='adsImage/%Y/%m/%d/', null=True, blank=True)
    ad_category = models.ForeignKey(AdsCategory, on_delete=models.CASCADE)
    ad_condition = models.CharField(max_length=250, choices=CONDITION_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ad_title} - {self.ad_category} - {self.created_at} - {self.is_active}"

    class Meta:
        db_table = 'advertiser'
        verbose_name = 'Advertiser'
        verbose_name_plural = 'Advertisers'
