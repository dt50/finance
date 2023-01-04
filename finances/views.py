from django.shortcuts import render
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from finances.models import Wallet, Finance, TypeFinance
from .forms import FinanceForm
from django_ajax.decorators import ajax
from django.http import JsonResponse
from orders.funcs.get_currency import get_currency


def is_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


@login_required(login_url="/users/sign/")
def index(request):
    photo = CustomUser.objects.get(user=request.user)
    form = FinanceForm()
    return render(
        request,
        "finances/index.html",
        {"url_photo": photo.avatar.url, "form": form},
    )


@ajax
def ajax_create_finance(request):
    if request.method == "POST" and is_ajax(request):
        form = FinanceForm(request.POST)
        finance = form.save(commit=False)
        if finance.budget < 0:
            finance.type_inout = 2
        finance.save()
        wallet = Wallet.objects.filter(customuser__user=request.user)[0]
        wallet.finance.add(finance)
        return JsonResponse({"state": "OK"})


@ajax
def ajax_delete_finance(request, id):
    finance = Finance.objects.get(id=id)
    finance.delete()


@ajax
def ajax_diff_budget(request):

    budget_curr = float(request.POST.get("diff_budget"))

    finances = Finance.objects.filter(wallet__customuser__user=request.user)
    user = CustomUser.objects.get(user=request.user)

    currency = get_currency()
    total_money = 0

    for finance in finances:
        if finance.currency == "2":
            total_money += finance.budget * float(currency["USD"]["Value"])
        elif finance.currency == "3":
            total_money += finance.budget * float(currency["EUR"]["Value"])
        else:
            total_money += finance.budget

    if budget_curr > total_money:
        diff = budget_curr - total_money
        type_ = TypeFinance.objects.get(name="Расхождение")
        finance = Finance(
            name="Расхождение +", budget=diff, type=type_, type_inout="1", currency="1"
        )
        finance.save()
        user.wallet.finance.add(finance)

    elif budget_curr < total_money:
        diff = total_money - budget_curr
        type_ = TypeFinance.objects.get(name="Расхождение")
        finance = Finance(
            name="Расхождение -", budget=diff, type=type_, type_inout="2", currency="1"
        )
        finance.save()
        user.wallet.finance.add(finance)
