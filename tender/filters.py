import django_filters
from .models import Tender

class TenderFilter(django_filters.FilterSet):
    created_datetime_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_datetime_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    deadline_datetime_after = django_filters.DateTimeFilter(field_name='deadline', lookup_expr='gte')
    deadline_datetime_before= django_filters.DateTimeFilter(field_name='deadline', lookup_expr='lte')

    class Meta:
        model = Tender
        fields = ['created_at', 'deadline']
        ordering_fields = ['name', 'created_at', 'deadline']