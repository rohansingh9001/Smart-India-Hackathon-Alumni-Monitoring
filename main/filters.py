from .models import AlumniDetailModel
import django_filters

class AlumniFilter(django_filters.FilterSet):
	Name = django_filters.CharFilter(lookup_expr='icontains')
	College = django_filters.CharFilter(lookup_expr='icontains')
	Year_Joined = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = AlumniDetailModel
		fields = ['Name', 'College', 'Year_Joined']