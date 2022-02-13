from django.contrib import admin

from petstagram.main.models import Profile, Pet, PetPhoto


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(PetPhoto)
class UserAdmin(admin.ModelAdmin):
    pass
