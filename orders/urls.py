from django.urls import path
from .views import index, ajax_create_order_view, ajax_delete_order
from . import ajax_datatable
from .ajax import (
    ajax_get_order,
    ajax_get_wishlist,
    ajax_update_order,
    ajax_update_wish,
    ajax_create_order,
    ajax_create_wish,
)


app_name = "orders"


urlpatterns = [
    path(
        "ajax_datatable/permissions/",
        ajax_datatable.OrdersDatatableView.as_view(),
        name="ajax_datatable_permissions",
    ),
    path(
        "ajax_datatable/wishlist/",
        ajax_datatable.WishlistDatatableView.as_view(),
        name="ajax_datatable_wishlist",
    ),
    path(
        "table/",
        index,
        name="index",
    ),
    path("create_order/", ajax_create_order_view, name="create_order"),
    path("ajax_delete_order/<int:id>", ajax_delete_order, name="ajax_delete_order"),
    path("ajax_order/", ajax_get_order, name="ajax_order"),
    path("ajax_wishlist/", ajax_get_wishlist, name="ajax_wishlist"),
    path("ajax_update_order/<int:id>", ajax_update_order, name="ajax_update_order"),
    path("ajax_update_wish/<int:id>", ajax_update_wish, name="ajax_update_wish"),
    path("ajax_create_order/", ajax_create_order, name="ajax_create_order"),
    path("ajax_create_wish/", ajax_create_wish, name="ajax_create_wish"),
]
