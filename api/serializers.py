from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import Blog, Mark


class MarksSerializer(ModelSerializer):
    class Meta:
        model = Mark
        fields = ("blog", "like", "reader")


class BlogsSerializer(ModelSerializer):
    # marks = MarksSerializer(many=True)
    # likes_count = serializers.SerializerMethodField()
    ann_likes = serializers.IntegerField()

    class Meta:
        model = Blog
        fields = ('id', 'ann_likes', 'title', 'text', 'image_blog', 'owner')

    # def get_likes_count(self, instance):
    #     return Mark.objects.filter(blog=instance, like=True).count()
