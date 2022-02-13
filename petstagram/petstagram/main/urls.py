from django.urls import path

from petstagram.main.views import display_home, display_dashboard, display_profile_details, display_photo_details


urlpatterns = (
    path('', display_home, name='index'),
    path('dashboard/', display_dashboard, name='dashboard'),
    path('profile/', display_profile_details, name='profile'),
    path('photo/details/', display_photo_details, name='photo'),  # <int:pk>/
)