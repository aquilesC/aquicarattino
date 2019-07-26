from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = verify_unique_slug(Category, self.name)
        super().save(args, kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = verify_unique_slug(Tag, self.name)
        super().save(args, kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    publish_time = models.DateTimeField(auto_now_add=False, null=True)
    last_edit_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = verify_unique_slug(Article, self.title)
        super().save(args, kwargs)

    def __str__(self):
        return self.title


def verify_unique_slug(cls, name):
    base_slug = slugify(name)
    slug = base_slug
    i = 1
    while cls.objects.filter(slug=slug).exists():
        slug = base_slug + '-' + str(i)
        i += 1
    return slug
