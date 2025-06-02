
from rest_framework import serializers
from .models import Arbitro

class ArbitrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbitro
        fields = '__all__'