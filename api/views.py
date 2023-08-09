from django.db.models import Count, Case, When
from rest_framework import viewsets
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers import BlogsSerializer, MarksSerializer
from main.models import Blog, Mark


class BlogsView(viewsets.ModelViewSet):
    serializer_class = BlogsSerializer
    queryset = Blog.objects.all().annotate(ann_likes=Count(Case(When(marks__like=True, then=1))))


class MarkView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Mark.objects.all()
    serializer_class = MarksSerializer
    lookup_field = 'blog'

    def get_object(self):
        obj, created = Mark.objects.get_or_create(
            reader=self.request.user, blog_id=self.kwargs['blog']
        )
        return obj
