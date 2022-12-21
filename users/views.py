from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from finances.models import Finance
from orders.funcs.get_img_site import get_img

from .forms import SignUpForm
from .models import CustomUser


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
    for finance in finances:
        total_money += finance.budget

    total_money_order = 0
    for order in user_finance.orders.all():
        total_money_order += order.price
        get_img(order.url)

    return render(
        request,
        "users/profile.html",
        {"info": user_finance, "money": total_money,
            "money_order": total_money_order},
    )
