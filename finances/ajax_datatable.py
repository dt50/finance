from ajax_datatable.views import AjaxDatatableView
from .models import Finance
from orders.funcs.get_currency import get_currency


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
            "choices": True,
            "autofilter": True,
        },
        {
            "name": "timestamp",
            "visible": True,
        },
        {
            "name": "type",
            "visible": True,
            "foreign_field": "type__name",
            "choices": True,
            "autofilter": True,
        },
        {
            "name": "type_inout",
            "visible": True,
            "className": "type_inout",
            "choices": True,
            "autofilter": True,
        },
        {
            "name": "delete",
            "title": "Delete",
            "placeholder": True,
            "searchable": False,
            "orderable": False,
        },
    ]

    def get_initial_queryset(self, request=None):
        queryset = Finance.objects.filter(
            wallet__customuser__user=request.user
        ).order_by("-timestamp")
        return queryset

    def customize_row(self, row, obj):
        row[
            "delete"
        ] = """
            <a href="#" class="btn btn-info btn-edit"
               onclick="
               const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
               var id=this.closest('tr').id.substr(4);
                $.ajax({
                    type: 'POST',
                    url :  `/ajax_delete_finance/${id}`,
                    headers: {'X-CSRFToken': csrftoken},
                    success : function(response){
                        $.fn.dataTable.tables({
                            api: true
                        }).draw();
                    },
                    error : function(response){
                        console.log(response)
                    }
                });
            ">
               Delete
            </a>
        """

    def footer_message(self, qs, params):
        currency = get_currency()
        total_money = 0
        for finance in qs:
            if finance.currency == "2":
                total_money += finance.budget * float(currency["USD"]["Value"])
            elif finance.currency == "3":
                total_money += finance.budget * float(currency["EUR"]["Value"])
            else:
                total_money += finance.budget
        return f"Current balance is {total_money}"
