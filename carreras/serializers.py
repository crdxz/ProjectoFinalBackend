from rest_framework import serializers
from .models import Carrera
from materias.models import Materia
from materias.serializers import MateriaSerializer

class CarreraSerializer(serializers.ModelSerializer):
    materias = MateriaSerializer(many=True)

    class Meta:
        model = Carrera
        fields = ('cod', 'nombre', 'materias')

    def create(self, validated_data):
        carrera = Carrera(nombre=validated_data.get('materias'))
        carrera.save()

        materias = validated_data.get('materias')

        for m in materias:
            Materia.objects.create(Carrera=carrera, **m)

        return validated_data
