from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название блога')
    owner = models.ForeignKey(User, related_name='blogs', on_delete=models.SET_NULL, null=True)
    text = models.TextField(verbose_name='Содержание')
    image_blog = models.ImageField(null=True, blank=True, default="default.jpg")

    def __str__(self):
        return self.title


class Mark(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="marks")
    like = models.BooleanField(default=False)
    reader = models.ForeignKey(User, related_name='Читатель', on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = [['reader', 'blog']]

    def __str__(self):
        return f"{self.reader} : {self.blog}"
