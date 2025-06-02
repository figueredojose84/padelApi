from django.urls import path, include
from rest_framework import routers
from equipos import views

router = routers.DefaultRouter()
router.register(r'equipos', views.EquipoView, 'equipos')

urlpatterns = [
    path('api/v1/', include(router.urls)),
   
]