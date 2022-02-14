from django.shortcuts import render, redirect

from petstagram.main.forms import CreateProfileForm, EditProfileForm
from petstagram.main.models import PetPhoto
from petstagram.main.helpers import get_profile


def display_profile_details(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects\
        .filter(tagged_animals__user_profile=profile)\
        .distinct()

    total_user_likes = sum(pp.likes for pp in pet_photos)
    total_user_pets_photos = len(pet_photos)

    context = {
        'profile': profile,
        'total_user_likes': total_user_likes,
        'total_user_pets_photos': total_user_pets_photos,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }
    return render(request, 'profile_create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(instance=profile)
        if form.is_valid():
            form.save()
            redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile_edit.html', context)


def delete_profile(request):

    return render(request, 'profile_delete.html')

