from rest_framework import viewsets
from .serializers import CarreraSerializer
from .models import Carrera

#Create your views here.

class CarreraView(viewsets.ModelViewSet):

    serializer_class =  CarreraSerializer
    queryset = Carrera.objects.all()
