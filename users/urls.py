from django.urls import path

from .views import (
    ajax_create_order,
    ajax_create_wish,
    ajax_get_order,
    ajax_get_wishlist,
    ajax_update_order,
    ajax_update_wish,
    auth,
    profile,
    register,
    sign,
    sign_out,
)

app_name = "users"

urlpatterns = [
    path("sign/", sign, name="sign"),
    path("login/", auth, name="login"),
    path("registration/", register, name="register"),
    path("sign-out/", sign_out, name="sign_out"),
    path("profile/", profile, name="profile"),
    path("ajax_order/", ajax_get_order, name="ajax_order"),
    path("ajax_wishlist/", ajax_get_wishlist, name="ajax_wishlist"),
    path("ajax_update_order/<int:id>",
         ajax_update_order, name="ajax_update_order"),
    path("ajax_update_wish/<int:id>", ajax_update_wish, name="ajax_update_wish"),
    path("ajax_create_order/", ajax_create_order, name="ajax_create_order"),
    path("ajax_create_wish/", ajax_create_wish, name="ajax_create_wish"),
]
