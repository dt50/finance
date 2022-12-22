from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import CustomUser
from finances.models import Finance
from orders.funcs.get_img_site import get_img
from orders.funcs.get_currency import get_currency
from django.db.models import Q


def sign(request):
    sign_in = AuthenticationForm()
    sign_up = SignUpForm()

    context = {"sign_in": sign_in, "sign_up": sign_up}
    return render(request, "users/registration.html", context)


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("finance:index")
    return redirect("users:sign")


def auth(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("finance:index")
    return redirect("users:sign")


def sign_out(request):
    logout(request)
    return redirect("users:sign")


def profile(request):
    user_finance = CustomUser.objects.get(user=request.user)
    finances = Finance.objects.filter(wallet__customuser__user=request.user)
    total_money = 0
    currency = get_currency()
    for finance in finances:
        if finance.currency == "2":
            total_money += finance.budget * float(currency["USD"]["Value"])
        elif finance.currency == "3":
            total_money += finance.budget * float(currency["EUR"]["Value"])
        else:
            total_money += finance.budget

    total_money_order = 0
    for order in user_finance.orders.filter(~Q(state__in=["2", "4"])):
        if order.currency == "2":
            total_money_order += order.price * float(currency["USD"]["Value"])
        elif order.currency == "3":
            total_money_order += order.price * float(currency["EUR"]["Value"])
        else:
            total_money_order += order.price
        get_img(order.url)

    total_money_wishlist = 0
    for wishlist in user_finance.wishlists.filter(~Q(state="2")):
        if wishlist.currency == "2":
            total_money_wishlist += wishlist.price * float(currency["USD"]["Value"])
        elif wishlist.currency == "3":
            total_money_wishlist += wishlist.price * float(currency["EUR"]["Value"])
        else:
            total_money_wishlist += wishlist.price
        get_img(wishlist.url)

    return render(
        request,
        "users/profile.html",
        {
            "info": user_finance,
            "money": round(total_money, 3),
            "money_order": round(total_money_order, 3),
            "money_wishlist": round(total_money_wishlist, 3),
        },
    )
