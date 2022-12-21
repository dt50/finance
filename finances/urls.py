from django.urls import include, path

from . import ajax_datatable
from .views import index

urlpatterns = [
    path("home/", index),
    path(
        "ajax_datatable/permissions/",
        ajax_datatable.PermissionAjaxDatatableView.as_view(),
        name="ajax_datatable_permissions",
    ),
]
