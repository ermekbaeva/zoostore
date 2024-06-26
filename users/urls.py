from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("logout/", views.logout, name="logout"),
    path('users_cart/', views.users_cart, name='users_cart')
]
