from django.contrib import admin
from .models import User, Ensemble, Song, Set, Track, Chart

# Register your models here.
admin.site.register(User)
admin.site.register(Ensemble)
admin.site.register(Song)
admin.site.register(Set)
admin.site.register(Track)
admin.site.register(Chart)