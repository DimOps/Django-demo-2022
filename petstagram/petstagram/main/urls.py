from django.urls import path

from petstagram.main.views import display_home, display_dashboard, display_profile_details, display_photo_details, \
    like_photo

urlpatterns = (
    path('', display_home, name='index'),
    path('dashboard/', display_dashboard, name='dashboard'),
    path('profile/', display_profile_details, name='profile'),
    path('photo/details/<int:pk>/', display_photo_details, name='photo'),
    path('photo/like/<int:pk>/', like_photo, name='like photo'),
)