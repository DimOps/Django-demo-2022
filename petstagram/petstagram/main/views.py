from django.shortcuts import render


def display_home(request):
    return render(request, 'home_page.html')


def display_dashboard(request):
    return render(request, 'dashboard.html')


def display_photo_details(request):
    return render(request, 'photo_details.html')


def display_profile_details(request):
    return render(request, 'profile_details.html')


def display_forbidden(request):
    return render(request, '401_error.html')