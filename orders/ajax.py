from django.core import serializers
from django.http import JsonResponse
from django_ajax.decorators import ajax

from finances.models import Finance, TypeFinance
from orders.forms import OrderForm, WishlistForm
from orders.models import Orders, Wishlist
from users.models import CustomUser


def is_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


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
        if instance.state == "2":
            user = CustomUser.objects.get(user=request.user)
            waste = TypeFinance.objects.get(name="Покупки")
            finance = Finance(
                name=instance.name,
                budget=f"-{instance.price}",
                type=waste,
                type_inout="2",
                currency=instance.currency,
            )
            finance.save()
            user.wallet.finance.add(finance)
        return JsonResponse({"state": "OK"}, status=200)


@ajax
def ajax_update_wish(request, id):
    if request.method == "POST" and is_ajax(request):
        instance = Wishlist.objects.get(id=id)
        form = WishlistForm(request.POST, instance=instance)
        form.save()
        if instance.state == "3":
            user = CustomUser.objects.get(user=request.user)
            instance = Wishlist.objects.get(id=id)
            order = Orders(
                state="3",
                name=instance.name,
                comment=instance.comment,
                url=instance.url,
                price=instance.price,
                currency=instance.currency,
            )
            order.save()
            user.orders.add(order)
        return JsonResponse({"state": "OK"}, status=200)


@ajax
def ajax_create_order(request):
    if request.method == "POST" and is_ajax(request):
        form = OrderForm(request.POST)
        order = form.save(commit=False)
        order.save()
        user = CustomUser.objects.get(user=request.user)
        user.orders.add(order)
        return JsonResponse({"state": "OK"}, status=200)


@ajax
def ajax_create_wish(request):
    if request.method == "POST" and is_ajax(request):
        form = WishlistForm(request.POST)
        wish = form.save(commit=False)
        wish.save()
        user = CustomUser.objects.get(user=request.user)
        user.wishlists.add(wish)
        return JsonResponse({"state": "OK"}, status=200)
