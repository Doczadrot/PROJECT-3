from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vehicle.apps import VehicleConfig
from .views import CarViewSet, MotoCreateAPIViews, MotoListAPIView, MotoRetriveAPIView, MotoUpdateAPIView, \
    MotoDestroyAPIView, MilageCreateAPIView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
    path('moto/create/', MotoCreateAPIViews.as_view(), name='moto-create'),
    path('moto/', MotoListAPIView.as_view(), name='moto-list'),
    path('moto/<int:pk>/', MotoRetriveAPIView.as_view(), name='moto-get'),
    path('moto/update/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto-update'),
    path('moto/delete/<int:pk>/', MotoDestroyAPIView.as_view(), name='moto-delete'),

    #milage
    path('milage/create/', MilageCreateAPIView.as_view(), name='milage-create'),

] + router.urls