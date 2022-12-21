from django.urls import path
from .views import sign, auth, register, sign_out, profile


app_name = "users"

urlpatterns = [
    path("sign/", sign, name="sign"),
    path("login/", auth, name="login"),
    path("registration/", register, name="register"),
    path("sign-out/", sign_out, name="sign_out"),
    path("profile/", profile, name="profile"),
]
