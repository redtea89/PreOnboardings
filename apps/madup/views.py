from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    GenericAPIView
)

from .serializers import (
    AdvertiserCLSerializer, AdvertiserRUDSerializer,
    AnalysisViewSerializer
)
from .models import Advertiser, AdvertisingData


class AdvertiserCLView(ListCreateAPIView):
    queryset = Advertiser
    serializer_class = AdvertiserCLSerializer


class AdvertiserRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Advertiser
    serializer_class = AdvertiserRUDSerializer


class AnalysisView(GenericAPIView):
    queryset = AdvertisingData
    serializer_class = AnalysisViewSerializer