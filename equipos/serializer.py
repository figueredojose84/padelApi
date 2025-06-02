
from rest_framework import serializers
from .models import Equipo

class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'