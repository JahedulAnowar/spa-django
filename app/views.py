from django.shortcuts import render 
from rest_framework import viewsets, serializers
from .models import Dog, Breed


class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = ['url', 'id', 'name', 'breed']


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ['url', 'id', 'name']


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all().order_by('name')
    serializer_class = DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all().order_by('name')
    serializer_class = BreedSerializer


def index(request): 
    return render(request, 'spa.html', {})
