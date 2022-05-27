from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    ListAPIView
)

from .models import Advertiser, AdvertisingData
from .filters import AnalysisFilter
from .serializers import AdvertiserCLSerializer, AdvertiserRUDSerializer


class AdvertiserCLView(ListCreateAPIView):
    """
    [GET] : 광고주 리스트 보기
    [POST] : 광고주 추가
    """
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserCLSerializer


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
        """
        Filtering한 queryset으로 
        분석데이터 구현해야하는 지점
        여기서 ORM을 얼마나 잘 쓰느냐에 따라 효율이 달라질 것으로 예상
        Madup 문제의 Key point
        시간이 좀 걸리므로 다른 작업을 진행하면서 천천히 생각해보겠음. 
        """
        return 1

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        analyzed_data = self._analyze_queryset(queryset)
        return Response(analyzed_data)
    