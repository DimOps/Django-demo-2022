from django.urls import path

from petstagram.main.views.generic import display_home, display_dashboard
from petstagram.main.views.pet_photos import display_photo_details, like_photo, create_pet_photo, edit_pet_photo
from petstagram.main.views.pets import create_pet, edit_pet, delete_pet
from petstagram.main.views.profiles import display_profile_details, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', display_home, name='index'),
    path('dashboard/', display_dashboard, name='dashboard'),

    path('profile/', display_profile_details, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/add/', create_pet, name='create pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),

    path('photo/details/<int:pk>/', display_photo_details, name='photo'),
    path('photo/like/<int:pk>/', like_photo, name='like photo'),
    path('photo/add/', create_pet_photo, name='create pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
)