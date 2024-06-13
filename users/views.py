from django.shortcuts import render

def login(request):
    context={
        "title": "Home"
    }
    return render(request, 'users/login.html', context)

def signup(request):
    context={
        "title": "Home"
    }
    return render(request, 'users/signup.html', context)

def profile(request):
    context={
        "title": "Home"
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    pass
