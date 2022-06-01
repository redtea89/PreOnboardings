from datetime import timedelta

from django.utils import timezone

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Research
from .serializers import *


class ResearchLimitOffPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'


class ResearchCLView(ListCreateAPIView):
    """
    [GET] : 임상정보 리스트 보기
    [POST] : 임상정보 추가
    """
    queryset = Research.objects.all()
    serializer_class = ResearchCLSerializer
    pagination_class = ResearchLimitOffPagination

    def get_queryset(self):
        param = self.request.GET.get('limit', None)
        papers = Research.objects.all()
        if param is None:
            return papers
        else:
            return papers.filter(updated_at__gte=(timezone.now() - timedelta(days=1)))


class ResearchRUDView(RetrieveUpdateDestroyAPIView):
    """
    [GET] : id로 개별 임상정보 보기
    [PUT] : id로 개별 임상정보 정보 업데이트
    [DELETE] : id로 개별 임상정보 삭제
    """
    queryset = Research.objects.all()
    serializer_class = ResearchRUDSerializer