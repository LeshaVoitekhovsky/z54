from django.db import models
from django.urls import reverse_lazy


class Post(models.Model):
    title = models.TextField()
    content = models.TextField(blank=True, null=True)
    hidden = models.BooleanField(default=False)

    def get_absolute_url(self) -> str:
        return reverse_lazy('single-post', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.title