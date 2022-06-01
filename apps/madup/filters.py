from datetime import datetime

from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import ValidationError


class AnalysisFilter(BaseFilterBackend):
    def _get_params(self, request):
        """
        Get params
        """
        advertiser_id = request.GET.get('advertiser_id', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        if advertiser_id is None:
            raise ValidationError("advertiser_id를 입력하세요.")
        if start_date is None:
            raise ValidationError("start_date를 입력하세요. YYYY-MM-DD형식")
        if end_date is None:
            raise ValidationError("end_date를 입력하세요. YYYY-MM-DD형식")

        params = {
            "advertiser_id": advertiser_id,
            "start_date": start_date,
            "end_date": end_date
        }
        return params

    def filter_queryset(self, request, queryset, view):
        """
        param 조건으로 ORM Filtering 적용
        """
        params = self._get_params(request)

        date_format = '%Y-%m-%d'
        start_date = datetime.strptime(params['start_date'], date_format).date()
        end_date = datetime.strptime(params['end_date'], date_format).date()

        objs = queryset.filter(
            advertiser__exact=params['advertiser_id'],
            date__gte=start_date,
            date__lte=end_date
        )
        return objs