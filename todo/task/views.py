from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

class TaskViewSet(ModelViewSet):
    queryset=Tasks.objects.all().order_by('-id')
    serializer_class=TaskSerializer
    
    
    def create(self,request,*args,**kwargs):
        if isinstance(request.data,list):
            serializer=self.get_serializer(data=request.data,many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return super().create(request,*args,**kwargs)