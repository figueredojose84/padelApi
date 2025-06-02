from django.urls import path, include
from rest_framework import routers
from arbitros import views

router = routers.DefaultRouter()
router.register(r'arbitros', views.ArbitroView, 'arbitros')

urlpatterns = [
    path('api/v1/', include(router.urls)),
   
]