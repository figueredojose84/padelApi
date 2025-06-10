from django.urls import path, include
from rest_framework import routers
from puntos import views

router = routers.DefaultRouter()
router.register(r'puntos', views.PuntoView, 'puntos')

urlpatterns = [
    path('api/v1/', include(router.urls)),
   
]