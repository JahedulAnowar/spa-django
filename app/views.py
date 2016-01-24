from django.shortcuts import render 
from rest_framework import viewsets, serializers
from .models import Dog, Breed


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ['url', 'id', 'name']


class DogSerializer(serializers.HyperlinkedModelSerializer):
    #breed = BreedSerializer(many=False, read_only=True)

    class Meta:
        model = Dog
        fields = ['url', 'id', 'name', 'breed']


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all().order_by('name')
    serializer_class = DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all().order_by('name')
    serializer_class = BreedSerializer


def index(request): 
    return render(request, 'spa.html', {})
