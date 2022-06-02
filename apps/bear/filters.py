from datetime import datetime
from datetime import timedelta

from django.db.models import Q, Sum, F
from django.db.models.functions import (
    ExtractHour, ExtractDay, ExtractWeek ,ExtractMonth, ExtractYear,
    TruncDate, TruncWeek,
)

from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import ValidationError

from .models import Pos, Group


class KpiPerRestaurantFilter(BaseFilterBackend):
    def _get_params(self, request):
            """
            Get params
            - params = "time_window", "number_of_party", "start_time", "end_time"
                "start_price", "end_price", "restaurant_name"
            """
            time_window = request.GET.get('time_window', None)
            start_time = request.GET.get('start_time', None)
            end_time = request.GET.get('end_time', None)
            start_price = request.GET.get('start_price', None)
            end_price = request.GET.get('end_price', None)
            restaurant_group = request.GET.get('restaurant_group', None)
            if time_window is None:
                raise ValidationError("time_window를 입력하세요.")
            if start_time is None:
                raise ValidationError("start_time를 입력하세요.")
            if end_time is None:
                raise ValidationError("end_time를 입력하세요.")
            
            # 날짜 포맷변환
            date_format = '%Y-%m-%d'
            end_time = datetime.strptime(end_time, date_format)
            end_time = end_time.date()

            params = {
                "time_window": time_window,
                "start_time": start_time,
                "end_time": end_time,
                "start_price": start_price,
                "end_price": end_price,
                "restaurant_group": restaurant_group
            }
            return params

    def filter_queryset(self, request, queryset, view):
        """
        param 조건으로 ORM Filtering 적용
        """
        params = self._get_params(request)
        time_windows = {
            'hour' : ExtractHour('timestamp'),
            'day'  : TruncDate('timestamp'),
            'week' : TruncWeek('timestamp'),
            'month': ExtractMonth('timestamp'),
            'year' : ExtractYear('timestamp')
        }
        
        if params['restaurant_group'] is not None:
            group = Group.objects.filter(name=params['restaurant_group']).first()

        
        q = Q()
        q &= Q(timestamp__range=(params['start_time'], params['end_time'] + timedelta(days=1)))
        if params['restaurant_group'] is not None:
            q &= Q(restaurant__group_id__exact=group)
        if (params['start_price'] is not None) and (params['end_price'] is not None):
            q &= Q(price__range=(int(params['start_price']), int(params['end_price'])))

        objs = Pos.objects.filter(q)\
                    .annotate(date=time_windows[params['time_window']]).values('date')\
                    .annotate(total_price=Sum('price'))
        return objs


class KpiPerPaymentFilter(BaseFilterBackend):
    """
    각 필터링을 적용하는 함수 넣기
    """
    pass

class KpiPerPartysizeFilter(BaseFilterBackend):
    """
    각 필터링을 적용하는 함수 넣기
    """
    pass