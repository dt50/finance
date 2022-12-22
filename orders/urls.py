from django.urls import path
from .views import index, ajax_create_order
from . import ajax_datatable


app_name = "orders"


urlpatterns = [
    path(
        "ajax_datatable/permissions/",
        ajax_datatable.PermissionAjaxDatatableView.as_view(),
        name="ajax_datatable_permissions",
    ),
    path(
        "table/",
        index,
        name="index",
    ),
    path("create_order/", ajax_create_order, name="create_order"),
]
