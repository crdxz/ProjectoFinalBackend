from rest_framework import serializers
from .models import Materia

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = (
            'cod', 'nombre', 'creditos', 'horas_td','horas_tc', 'horas_ta',
        )
