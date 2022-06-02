from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)

from .models import Group, Restaurant, Pos
from .serializers import *
from .filters import *


class KpiPerRestaurantView(ListAPIView):
    """
    [GET] time window와 그룹이름과 기간과 가격범위로 레스토랑별 총 매출 리턴
     - params[필수] = "time_window", "start_time", "end_time"
     - params[옵션] = "start_price", "end_price", "Restaurant_group"
    """
    queryset = Pos.objects.all()
    filter_backends = [KpiPerRestaurantFilter]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        result = queryset.values(
            'date',
            'restaurant_id',
            'total_price',
            )
        return Response(result)


class KpiPerPaymentView(ListAPIView):
    """
    [GET] time window와 그룹이름과 기간과 가격범위로 레스토랑별 총 매출 리턴
     - params = "time_window", "number_of_party", "start_time", "end_time"
                "start_price", "end_price", "group_name"
    """
    queryset = Pos.objects.all()
    filter_backends = [KpiPerPaymentFilter]

    def _analyze_queryset(self, queryset):
        # 필터링된 queryset을 ORM을 이용하여 분석하는 단계
        # 베어로보틱스 문제의 핵심 Point
        return 1

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        analyzed_data = self._analyze_queryset(queryset)
        return Response(analyzed_data)


class KpiPerPartysizeView(ListAPIView):
    """
    [GET] time window와 그룹이름과 기간과 가격범위로 레스토랑별 총 매출 리턴
     - params = "time_window", "number_of_party", "start_time", "end_time"
                "start_price", "end_price", "group_name"
    """
    queryset = Pos.objects.all()
    filter_backends = [KpiPerPartysizeFilter]

    def _analyze_queryset(self, queryset):
        # 필터링된 queryset을 ORM을 이용하여 분석하는 단계
        # 베어로보틱스 문제의 핵심 Point
        return 1

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        analyzed_data = self._analyze_queryset(queryset)
        return Response(analyzed_data)


class GroupCLView(ListCreateAPIView):
    """
    [GET] : 프랜차이즈 그룹 리스트 보기
    [POST] : 프랜차이즈 그룹 추가
    """
    queryset = Group.objects.all()
    serializer_class = GroupCLSerializer


class GroupRUDView(RetrieveUpdateDestroyAPIView):
    """
    [GET] : id로 개별 프랜차이즈 그룹 보기
    [PUT] : id로 개별 프랜차이즈 그룹 정보 업데이트
    [DELETE] : id로 개별 프랜차이즈 그룹 삭제
    """
    queryset = Group.objects.all()
    serializer_class = GroupRUDSerializer


class RestaurantCLView(ListCreateAPIView):
    """
    [GET] : 점포 리스트 보기
    [POST] : 점포 추가
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCLSerializer


class RestaurantRUDView(RetrieveUpdateDestroyAPIView):
    """
    [GET] : id로 개별 점포 보기
    [PUT] : id로 개별 점포 정보 업데이트
    [DELETE] : id로 개별 점포 삭제
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantRUDSerializer