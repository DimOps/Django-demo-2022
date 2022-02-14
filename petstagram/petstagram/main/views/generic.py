from django.shortcuts import render

from petstagram.main.models import PetPhoto
from petstagram.main.helpers import get_profile


def display_home(request):
    context = {
        'hide_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def display_dashboard(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects \
        .prefetch_related('tagged_animals') \
        .filter(tagged_animals__user_profile=profile) \
        .distinct()

    context = {
        'pet_photos': pet_photos
    }

    return render(request, 'dashboard.html', context)