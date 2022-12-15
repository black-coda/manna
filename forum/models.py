from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Forum(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} ({self.creator.username})"

    def save(self, *args, **kwargs):
        value = self.topic
        if value is not None:
            self.slug = slugify(value, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('forum-detail', kwargs={'slug': self.slug})


class Messages(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    forum = models.ForeignKey(Forum, on_delete=models.SET_NULL, null=True, default="Anonymous")

    def __str__(self):
        return f"{self.user.username} ({self.body[:30]})"

    class Meta:
        verbose_name_plural = "messages"
