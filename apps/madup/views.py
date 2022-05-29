from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)

from .models import Advertiser, AdvertisingData
from .filters import AnalysisFilter
from .serializers import AdvertiserCLSerializer, AdvertiserRUDSerializer


class AdvertiserPagination(PageNumberPagination):
    page_size = 10


class AdvertiserCLView(ListCreateAPIView):
    """
    [GET] : 광고주 리스트 보기
    [POST] : 광고주 추가
    """
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserCLSerializer
    pagination_class = AdvertiserPagination


class AdvertiserRUDView(RetrieveUpdateDestroyAPIView):
    """
    [GET] : id로 개별 광고주 보기
    [PUT] : id로 개별 광고주 정보 업데이트
    [DELETE] : id로 개별 광고주 삭제
    """
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserRUDSerializer


class AnalysisView(ListAPIView):
    """
    [GET] 광고주 id와 기간으로 매체별 통계량 리턴
     - params = "advertiser_id", "start_date", "end_date"
    """
    queryset = AdvertisingData.objects.all()
    filter_backends = [AnalysisFilter]

    def _analyze_queryset(self, queryset):
        a = 1
        # queryset의 media 종류를 가져온다. 

        # 각 미디어별로 연산을 진행한다. 

        # 진행한 연산을 result = {} 의 집합으로 집어넣는다. 

        return 1

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        analyzed_data = self._analyze_queryset(queryset)
        return Response(analyzed_data)
    