import django_filters
from .models import News

class NewsFilter(django_filters.FilterSet):
    created_datetime_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_datetime_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    class Meta:
        model = News
        fields = ['created_at']
        ordering_fields = ['title_ru','title_kg','title_en', 'created_at']