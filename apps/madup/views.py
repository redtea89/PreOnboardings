from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    ListAPIView
)

from .serializers import (
    AdvertiserCLSerializer, AdvertiserRUDSerializer,
    AnalysisViewSerializer
)
from .models import Advertiser, AdvertisingData


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
    queryset = AdvertisingData.objects.all()
    serializer_class = AnalysisViewSerializer

    