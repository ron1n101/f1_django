from django.contrib import admin
from .models import Team, Gallery, Feedback


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name_team',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Feedback)
class FeedbackAdm(admin.ModelAdmin):
    list_display = ('email',)