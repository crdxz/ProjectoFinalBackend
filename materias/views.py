from logging import raiseExceptions
from rest_framework import viewsets
from rest_framework.views import APIView 
from django.http import FileResponse

from .serializers import MateriaSerializer
from .models import Materia

from proyectoFinal.settings import BASE_DIR
import os

#Create your views here.

class MateriaView(viewsets.ModelViewSet):

    serializer_class =  MateriaSerializer
    queryset = Materia.objects.all()


class syllabusFile(APIView):

    def post(self, request, *args, **kwargs):
        carrera = request.data.get("carrera", "")
        codigo = request.data.get("codigo", "")

        ruta = os.path.join(BASE_DIR,"src","syllabus", carrera+codigo+".pdf")

        try:
            return FileResponse(open(ruta, "rb"))
        except:
            return raiseExceptions
