from ajax_datatable.views import AjaxDatatableView

from .models import Orders


class PermissionAjaxDatatableView(AjaxDatatableView):
    model = Orders
    title = "Orders"
    initial_order = [
        ["timestamp", "desc"],
    ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, "all"]]
    search_values_separator = "+"

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {
            "name": "id",
            "visible": False,
        },
        {"name": "state", "visible": True, "className": "state"},
        {"name": "name", "visible": True, "className": "name"},
        {"name": "url", "visible": True, "className": "url"},
        {
            "name": "price",
            "visible": True,
        },
        {"name": "currency", "visible": True},
        {"name": "date_buy", "visible": True},
        {"name": "timestamp", "visible": True},
    ]

    def get_initial_queryset(self, request=None):
        queryset = Orders.objects.filter(customuser__user=request.user).order_by(
            "-timestamp"
        )
        return queryset
