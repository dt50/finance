from django.urls import path, include
from .views import index
from . import ajax_datatable


app_name = 'finance'

urlpatterns = [
    path("home/", index, name='index'),
    path(
        "ajax_datatable/permissions/",
        ajax_datatable.PermissionAjaxDatatableView.as_view(),
        name="ajax_datatable_permissions",
    ),
]
