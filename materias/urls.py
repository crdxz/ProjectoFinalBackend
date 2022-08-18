from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MateriaView, syllabusFile

router = DefaultRouter()
router.register(r'materias', MateriaView, basename="materias")

urlpatterns = [
    path('',include(router.urls)),
    path('syllabus/', syllabusFile.as_view())

]
