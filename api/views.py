from rest_framework import viewsets

from api.serializers import BlogsSerializer
from main.models import Blog


class BlogsView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer