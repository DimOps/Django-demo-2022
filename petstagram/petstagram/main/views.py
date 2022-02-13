from django.shortcuts import render, redirect

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
    pet_photos = set(PetPhoto.objects.filter(tagged_animals__user_profile=profile))
    context = {
        'pet_photos': pet_photos
    }
    return render(request, 'dashboard.html', context)


def display_photo_details(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo', pk)


def display_profile_details(request):
    return render(request, 'profile_details.html')


def display_forbidden(request):
    return render(request, '401_error.html')