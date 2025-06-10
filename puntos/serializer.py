
from rest_framework import serializers
from .models import Punto

class PuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punto
        fields = '__all__'