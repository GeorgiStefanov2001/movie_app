from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('General Information', {'fields': ['genre','rating','release_date']}),
        ('Other', {'fields': ['description']}),
    ]

admin.site.register(Movie, MovieAdmin)

