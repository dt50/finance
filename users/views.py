from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django_ajax.decorators import ajax

from finances.models import Finance
from orders.forms import OrderForm, WishlistForm
from orders.funcs.get_currency import get_currency
from orders.funcs.get_img_site import get_img
from orders.models import Orders, Wishlist

from .forms import SignUpForm
from .models import CustomUser


def is_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


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
    order_form = OrderForm()
    wishlist_form = WishlistForm()
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
            total_money_wishlist += wishlist.price * \
                float(currency["USD"]["Value"])
        elif wishlist.currency == "3":
            total_money_wishlist += wishlist.price * \
                float(currency["EUR"]["Value"])
        else:
            total_money_wishlist += wishlist.price
        get_img(wishlist.url)

    return render(
        request,
        "users/profile.html",
        {
            "info": user_finance,
            "order_form": order_form,
            "wishlist_form": wishlist_form,
            "money": round(total_money, 3),
            "money_order": round(total_money_order, 3),
            "money_wishlist": round(total_money_wishlist, 3),
        },
    )


def ajax_get_order(request):
    id = request.GET.get("id")
    try:
        order = Orders.objects.get(id=id)
    except Orders.DoesNotExist:
        return JsonResponse(data={"status": "error"}, status=400)
    serialized_obj = serializers.serialize("python", [order])
    return JsonResponse(data=serialized_obj, safe=False)


def ajax_get_wishlist(request):
    id = request.GET.get("id")
    try:
        wishlist = Wishlist.objects.get(id=id)
    except Wishlist.DoesNotExist:
        return JsonResponse(data={"status": "error"}, status=400)
    serialized_obj = serializers.serialize("python", [wishlist])
    return JsonResponse(data=serialized_obj, safe=False)


@ajax
def ajax_update_order(request, id):
    if request.method == "POST" and is_ajax(request):
        instance = Orders.objects.get(id=id)
        form = OrderForm(request.POST, instance=instance)
        form.save()
        return JsonResponse({"state": "OK"}, status=200)


@ajax
def ajax_update_wish(request, id):
    if request.method == "POST" and is_ajax(request):
        instance = Wishlist.objects.get(id=id)
        form = WishlistForm(request.POST, instance=instance)
        form.save()
        return JsonResponse({"state": "OK"}, status=200)
