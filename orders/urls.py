from django.urls import path

from . import ajax_datatable
from .views import ajax_create_order, index

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
