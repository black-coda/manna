from django.contrib import admin
from .models import User, Manna
from django.contrib.auth.admin import UserAdmin





@admin.register(Manna)
class MannaAdmin(admin.ModelAdmin):
    list_display = ('title','user',)
    list_filter = ('created', 'user')
    search_fields = ('title', 'user')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'created'
    ordering = ('-updated', '-created')

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'avatar',
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                'email','avatar',
            ),
        }),
    )    