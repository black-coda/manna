from django.contrib import admin
from .models import User, Manna
from django.contrib.auth.admin import UserAdmin
admin.site.register(User, UserAdmin)



class MannaAdmin(admin.ModelAdmin):
    list_display = ('title', 'keyverses', 'user',)
    list_filter = ('created','keyverses', 'user')
    search_fields = ('title', 'user')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'created'
    ordering = ('-updated', '-created')
admin.site.register(Manna,MannaAdmin)