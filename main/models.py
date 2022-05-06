from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify

def user_directory_path(instance, image_file):
    return 'user_{0}/{1}'.format(instance.full_name, image_file)


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Manna(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    category = models.CharField(help_text='e.g Prayer upliftment, Charge on Faith', max_length=30, default='Christian Charge')
    thumbnail = models.ImageField(upload_to='thumbnail/')
    body = models.TextField()
    keyverses = models.TextField(help_text='Write each key verse seperated by a comma')
    slug = models.SlugField(default=' ', max_length=200,blank=True  )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'manna'

    def get_absolute_url(self):
        return reverse("detail-view", kwargs={"slug": self.slug})
    
    def save(self,*args, **kwargs):
        value = self.title
        self.slug = slugify(value,allow_unicode=True)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f'{self.title} {self.user}'
    

class Comment(models.Model):
    manna = models.ForeignKey(Manna, on_delete=models.CASCADE, related_name='manna_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created','-updated']

    def __str__(self):
        return f'{self.manna} {self.user}'
    
