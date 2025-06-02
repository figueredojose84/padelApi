from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import ArbitrosSerializer
from .models import Arbitro

class ArbitroView(viewsets.ModelViewSet):
    serializer_class = ArbitrosSerializer
    queryset = Arbitro.objects.all()

