from django.contrib.postgres.search import SearchQuery
from django_filters import Filter
from django_filters.constants import EMPTY_VALUES


class ListFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value_list = value.split(u',')
        self.lookup_expr = 'in'
        return super().filter(qs, value_list)


class FullTextSearchFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        if self.distinct:
            qs = qs.distinct()
        qs = self.get_method(qs)(**{self.field_name: SearchQuery(value, config='english')})
        return qs


class ArrayFieldFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value_list = value.split(u',')
        return super().filter(qs, value_list)
