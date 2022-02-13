from django.shortcuts import render

from petstagram.main.models import Profile, PetPhoto


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None

def display_home(request):
    context = {
        'hide_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def display_dashboard(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects.filter(tagged_animals__user_profile=profile)
    context = {
        'pet_photos': pet_photos
    }
    return render(request, 'dashboard.html', context)


def display_photo_details(request):
    return render(request, 'photo_details.html')


def display_profile_details(request):
    return render(request, 'profile_details.html')


def display_forbidden(request):
    return render(request, '401_error.html')