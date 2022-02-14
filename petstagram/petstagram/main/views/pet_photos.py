from django.shortcuts import render, redirect

from petstagram.main.models import PetPhoto


def display_photo_details(request, pk):
    pet_photo = PetPhoto.objects\
        .prefetch_related('tagged_animals')\
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo', pk)


def create_pet_photo(request):
    return render(request, 'photo_create.html')


def edit_pet_photo(request):
    return render(request, 'photo_edit.html')