from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=255,
                            blank=True,
                            unique=True)

    def __str__(self):
        return f"{self.author} - {self.title}"

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f"{self.author}-{self.title}")
        return super().save(force_insert, force_update, using, update_fields)
