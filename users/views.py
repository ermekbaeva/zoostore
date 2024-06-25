from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, login successful")
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "Home",
        "form": form,
    }
    return render(request, "users/login.html", context)


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username},sign up successful")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Home", "form": form}
    return render(request, "users/signup.html", context)

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)
    context = {"title": "Home", "form": form}
    return render(request, "users/profile.html", context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "logout successful")
    return redirect(reverse("main:index"))
