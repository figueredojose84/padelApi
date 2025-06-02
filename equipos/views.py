from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import EquiposSerializer
from .models import Equipo

class EquipoView(viewsets.ModelViewSet):
    serializer_class = EquiposSerializer
    queryset = Equipo.objects.all()
