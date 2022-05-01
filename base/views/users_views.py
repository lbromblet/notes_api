from django.shortcuts import render


def loginPage(request):
    return render(request, 'users/login_register.html')