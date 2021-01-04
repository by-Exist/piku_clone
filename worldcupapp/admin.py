from django.contrib import admin
from .models import WorldCup, Player


@admin.register(WorldCup)
class WorldCupAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class ImageAdmin(admin.ModelAdmin):
    pass