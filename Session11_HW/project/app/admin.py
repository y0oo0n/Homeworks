from django.contrib import admin
from .models import Song, Comment

# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment)