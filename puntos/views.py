from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import PuntosSerializer
from .models import Punto

class PuntoView(viewsets.ModelViewSet):
    serializer_class = PuntosSerializer
    queryset = Punto.objects.all()

