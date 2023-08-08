from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import Blog, Mark


class MarksSerializer(ModelSerializer):
    class Meta:
        model = Mark
        fields = ("blog", "like", "reader")


class BlogsSerializer(ModelSerializer):
    marks = MarksSerializer(many=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = "__all__"

    def get_likes_count(self, instance):
        return Mark.objects.filter(blog=instance, like=True).count()
