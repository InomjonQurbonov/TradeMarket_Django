from django.urls import path
from app_ads.views import (
    AdvertiserListView, AdvertiserDetailView, AdvertiserCreateView,
    AdvertiserUpdateView, AdvertiserDeleteView, SwapOfferCreateView,
    SwapOfferUpdateView, LoginView, RegisterView, LogoutView
)

urlpatterns = [
    # Веб-интерфейс для объявлений
    path('', AdvertiserListView.as_view(), name='advertiser-list'),
    path('advertiser/<int:pk>/', AdvertiserDetailView.as_view(), name='advertiser-detail'),
    path('advertiser/create/', AdvertiserCreateView.as_view(), name='advertiser-create'),
    path('advertiser/<int:pk>/update/', AdvertiserUpdateView.as_view(), name='advertiser-update'),
    path('advertiser/<int:pk>/delete/', AdvertiserDeleteView.as_view(), name='advertiser-delete'),
    path('advertiser/<int:ad_id>/swap-offer/', SwapOfferCreateView.as_view(), name='swap-offer-create'),
    path('advertiser/<int:target_ad_id>/swap-offer/<int:pk>/update/', SwapOfferUpdateView.as_view(), name='swap-offer-update'),
    # Аутентификация
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]