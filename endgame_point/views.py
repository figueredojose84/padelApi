from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import PointSerializer
from .models import Point

class PointView(viewsets.ModelViewSet):
    serializer_class = PointSerializer
    queryset = Point.objects.all()
