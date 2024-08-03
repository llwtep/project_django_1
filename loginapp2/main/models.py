import os.path

from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-post', kwargs={'pk': self.pk})
    def delete(self,*args, **kwargs):
        if self.post_image:
            if os.path.isfile(self.post_image.path):
                os.remove(self.post_image.path)
            super().delete(*args, **kwargs)
















