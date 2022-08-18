from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CarreraView 

router = DefaultRouter()
router.register(r'carreras', CarreraView, basename="carreras")

urlpatterns = [
    path('',include(router.urls)),
]
