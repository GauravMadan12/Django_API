from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

