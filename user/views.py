from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
