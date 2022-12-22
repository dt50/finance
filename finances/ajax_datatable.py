from ajax_datatable.views import AjaxDatatableView

from .models import Finance


class PermissionAjaxDatatableView(AjaxDatatableView):
    model = Finance
    title = "Finances"
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
        {"name": "budget", "visible": True, "className": "budget"},
        {
            "name": "currency",
            "visible": True,
        },
        {
            "name": "timestamp",
            "visible": True,
        },
        {
            "name": "type",
            "visible": True,
        },
        {"name": "type_inout", "visible": True, "className": "type_inout"},
    ]

    def get_initial_queryset(self, request=None):
        queryset = Finance.objects.filter(
            wallet__customuser__user=request.user
        ).order_by("-timestamp")
        return queryset
