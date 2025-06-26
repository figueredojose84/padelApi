from django.urls import path, include
from rest_framework import routers
from endgame_point import views

router = routers.DefaultRouter()
router.register(r'endgame_point', views.PointView, 'endgame_point')

urlpatterns = [
    path('api/v1/', include(router.urls)),
   
]