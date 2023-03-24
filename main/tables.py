import django_tables2 as tables
from .models import History

ATTRIBUTES = {
    "th": {
        "_ordering": {
            "orderable": "sortable", # Instead of `orderable`
            "ascending": "ascend",   # Instead of `asc`
            "descending": "descend"  # Instead of `desc`
        }
    }
}


class HistoryTable(tables.Table):
    class Meta:
        my_column = tables.Column()
        model = History
        attrs = {'class': 'paleblue'}
        fields = ("operation_type", "creation_time", "equation", "result", )
        #country = tables.Column(footer="Total:")


