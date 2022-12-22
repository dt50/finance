from django.http import JsonResponse
from django.shortcuts import render
from django_ajax.decorators import ajax

from finances.models import Finance, TypeFinance
from users.models import CustomUser

from .forms import OrderForm


def is_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


def index(request):
    photo = CustomUser.objects.get(user=request.user)
    form = OrderForm()
    return render(
        request,
        "orders/table.html",
        {"url_photo": photo.avatar.url, "form": form},
    )


@ajax
def ajax_create_order(request):
    if request.method == "POST" and is_ajax(request):
        form = OrderForm(request.POST)
        order = form.save(commit=False)
        order.save()
        user = CustomUser.objects.get(user=request.user)
        user.orders.add(order)
        waste = TypeFinance.objects.get(name="Покупки")
        finance = Finance(
            name=order.name,
            budget=f"-{order.price}",
            type=waste,
            type_inout="2",
            currency=order.currency,
        )
        finance.save()
        user.wallet.finance.add(finance)
        return JsonResponse({"state": "OK"})
