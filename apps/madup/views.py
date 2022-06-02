from django.db.models import Sum

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
        # queryset의 media 종류를 가져온다. 
        objs = queryset.values_list('media', flat=True).distinct()
        media_kind_list = []
        for i, obj in enumerate(objs):
        # for i in range(objs.count()):
            media_kind_list.append(objs[i])

        
        # 진행한 연산을 result = {} 의 집합으로 집어넣는다. 
        analysis_datas_set = {}
        for kind in media_kind_list:
            data = objs.filter(media=kind)
            total = objs.aggregate(
                total_click = Sum('click'),
                total_impression = Sum('impression'),
                total_cost = Sum('cost'),
                total_conversion = Sum('conversion'),
                total_cv = Sum('cv'),
            )

            analysis_datas = {
                'ctr': 0 if total['total_impression'] == 0 else round(total['total_click'] * 100 / total['total_impression'], 2),
                'roas': 0 if total['total_cost'] == 0 else round(total['total_cv'] * 100 / total['total_cost'], 2),
                'cpc': 0 if total['total_click'] == 0 else round(total['total_cost'] * 100 / total['total_click'], 2),
                'cvr': 0 if total['total_click'] == 0 else round(total['total_conversion'] * 100 / total['total_click'], 2),
                'cpa': 0 if total['total_conversion'] == 0 else round(total['total_cost'] * 100 / total['total_conversion'], 2),
            }
            analysis_datas_set[f'{kind}'] = analysis_datas

        return analysis_datas_set

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        analyzed_data = self._analyze_queryset(queryset)
        return Response(analyzed_data)