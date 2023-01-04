from django.urls import path, include
from .views import index, ajax_create_finance, ajax_delete_finance, ajax_diff_budget
from . import ajax_datatable


app_name = "finance"

urlpatterns = [
    path("home/", index, name="index"),
    path(
        "ajax_datatable/permissions/",
        ajax_datatable.PermissionAjaxDatatableView.as_view(),
        name="ajax_datatable_permissions",
    ),
    path("append_finance/", ajax_create_finance, name="append_finance"),
    path(
        "ajax_delete_finance/<int:id>", ajax_delete_finance, name="ajax_delete_finance"
    ),
    path("ajax_diff_budget/", ajax_diff_budget, name="ajax_diff_budget"),
]
