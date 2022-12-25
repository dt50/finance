from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django_ajax.decorators import ajax

from finances.models import Finance, Wallet
from users.models import CustomUser

from .forms import FinanceForm


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
