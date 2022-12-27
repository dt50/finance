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
        {
            "name": "delete",
            "title": "Delete",
            "placeholder": True,
            "searchable": False,
            "orderable": False,
        },
    ]

    def get_initial_queryset(self, request=None):
        queryset = Orders.objects.filter(customuser__user=request.user).order_by(
            "-timestamp"
        )
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
                    url :  `/orders/ajax_delete_order/${id}`,
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
        row["timestamp"] = f"{obj.timestamp.date()}"
