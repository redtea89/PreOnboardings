from datetime import datetime

from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import ValidationError


class KpiPerRestaurantFilter(BaseFilterBackend):
    """
    각 필터링을 적용하는 함수 넣기
    """
    pass


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