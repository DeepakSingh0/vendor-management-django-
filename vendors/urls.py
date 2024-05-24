# urls.py
from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDestroy

urlpatterns = [
    path('api/vendors/', VendorListCreate.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroy.as_view(), name='vendor-detail'),
]
