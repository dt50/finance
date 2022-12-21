from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission

from .models import Finance, Wallet


class PermissionAjaxDatatableView(AjaxDatatableView):
    model = Finance
    title = "Finances"
    initial_order = [
        ["budget", "asc"],
    ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, "all"]]
    search_values_separator = "+"

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {
            "name": "id",
            "visible": False,
        },
        {
            "name": "budget",
            "visible": True,
        },
        {
            "name": "currency",
            "visible": True,
        },
        {
            "name": "timestamp",
            "visible": True,
        },
    ]

    def get_initial_queryset(self, request=None):
        queryset = Finance.objects.filter(
            wallet__customuser__user=request.user)
        return queryset
