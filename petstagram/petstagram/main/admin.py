from django.contrib import admin

from petstagram.main.models import Profile, Pet


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class UserAdmin(admin.ModelAdmin):
    pass