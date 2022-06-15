from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


def user_directory_path(instance, image_file):
    return 'user_{0}/{1}'.format(instance.get_full_name(), image_file)


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True, default='default/avatar.svg')
    bio = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("profile", args=[str(self.username)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Manna(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    title = models.CharField(max_length=50, unique=True)
    category = models.CharField(help_text='e.g Prayer charge, Charge on Faith', max_length=30,
                                default='Christian Charge')
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)
    body = models.TextField()
    slug = models.SlugField(default=' ', max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    bible_verses = models.CharField(max_length=200,
                                    help_text='Enter the book of the bible(in full please like Hebrew)',
                                    null=True)
    chapter_of_bible_verse = models.IntegerField(blank=True, null=True)

    verse_of_chapter = models.CharField(blank=True, null=True, max_length=20)

    display_verse = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'manna'
        ordering = ['?']

    def get_absolute_url(self):
        return reverse("detail-view", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} {self.user}'


class Comment(models.Model):
    manna = models.ForeignKey(Manna, on_delete=models.CASCADE, related_name='manna_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return f'{self.manna} {self.user}'
