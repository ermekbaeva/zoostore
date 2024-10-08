from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import (
    ProfileForm,
    UserLoginForm,
    UserRegistrationForm,
    CustomPasswordChangeForm,
)
from django.contrib.auth import update_session_auth_hash
from django.db.models import Prefetch


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            session_key=request.session.session_key
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, login successful")
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse("user:logout"):
                    return HttpResponseRedirect(request.POST.get("next"))
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
            session_key=request.session.session_key
            user = form.instance
            auth.login(request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
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
            messages.success(request, "Your profile was successfully updated!")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    orders = (Order.objects.filter(user=request.user).prefetch_related(Prefetch("orderitem_set", queryset = OrderItem.objects.select_related("product"),)).order_by("-id"))
    context = {"title": "Home", "form": form, "orders": orders}
    return render(request, "users/profile.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("user:profile")
    else:
        form = CustomPasswordChangeForm(user=request.user)

    context = {
        "form": form,
    }
    return render(request, "user/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "logout successful")
    return redirect(reverse("main:index"))


def users_cart(request):
    return render(request, "users/users_cart.html")
