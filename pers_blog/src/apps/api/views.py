from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.blog.models import BlogModel
from apps.users.models import UsersModel
from apps.api.serializers import UsersModelSerializer, BlogModelSerializer

# Create your views here.
class BlogModelViewset(ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        return [permission() for permission in permission_classes]

class UsersModelViewset(ModelViewSet):
    queryset = UsersModel.objects.all()
    serializer_class = UsersModelSerializer