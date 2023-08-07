from rest_framework.serializers import ModelSerializer

from main.models import Blog


class BlogsSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"

