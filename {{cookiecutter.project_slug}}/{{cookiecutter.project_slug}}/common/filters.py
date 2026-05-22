from django_filters import Filter
from django_filters.constants import EMPTY_VALUES
{% if cookiecutter.use_postgres == 'y' -%}
from django.contrib.postgres.search import SearchQuery
{%- endif %}


class ListFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value_list = value.split(u',')
        self.lookup_expr = 'in'
        return super().filter(qs, value_list)


{% if cookiecutter.use_postgres == 'y' -%}
class FullTextSearchFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        if self.distinct:
            qs = qs.distinct()
        qs = self.get_method(qs)(**{self.field_name: SearchQuery(value, config='english')})
        return qs


{% endif -%}
class ArrayFieldFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value_list = value.split(u',')
        return super().filter(qs, value_list)
