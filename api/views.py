from django.shortcuts import render
from rest_framework import generics
from api.custom_renderers import JPEGrenderers, PNGrenderers
from images.models import Images
from rest_framework.response import Response
# Create your views here.

class ImageAPIView(generics.RetrieveAPIView):
    
    renderer_classes = [JPEGrenderers ]
    
    def get(self, request, *args, **kwargs):
        queryset = Images.objects.get(id= self.kwargs['id']).image
        data = queryset
        return Response(data, content_type = 'image/jpg')