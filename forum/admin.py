from django.contrib import admin
from . import models


admin.site.register(models.Forum)
admin.site.register(models.Messages)
admin.site.register(models.Topic)
